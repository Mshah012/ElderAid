from django.shortcuts import render,redirect
from .forms import BookingForm,bookings
from django.http import HttpResponse
from elder_services.models import * 
from .decorators import custom_login_required
# Create your views here.

@custom_login_required
def my_bookings(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Or your login route

    user = user_info.objects.get(pk=user_id)
    all_bookings = bookings.objects.filter(user_id=user).order_by('-from_date', '-booking_time')
  # Latest first

    return render(request, 'elder_bookings/my_bookings.html', {
        'user': user,
        'bookings': all_bookings
    })
    
def book_service(request):
    context= {'services_list': services.objects.all()}
    return render(request,"elder_bookings/service_choice.html",context)

def book_subservice(request,id):
    context= {'subservices_list': sub_services.objects.filter(service_id_id=id)}
    return render(request,"elder_bookings/subservice_choice.html",context)

@custom_login_required
def booking_confirm(request,id):
    if request.method=='GET':
        form=BookingForm()
        return render(request,'elder_bookings/booked_service.html',{'form':form})
    else:
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)

            user_id = request.session.get("user_id")
        if not user_id:
            return HttpResponse("User not logged in", status=401)

    try:
        user = user_info.objects.get(pk=user_id)
        sub = sub_services.objects.get(pk=id)
    except user_info.DoesNotExist:
        return HttpResponse("User not found", status=404)
    except sub_services.DoesNotExist:
        return HttpResponse("Sub-service not found", status=404)

    booking.user_id = user
    booking.subservice_id = sub
    booking.service_id = sub.service_id
    booking.price = sub.price
    
    days = (booking.to_date - booking.from_date).days + 1  # inclusive range
    if days <= 0:
        return HttpResponse("Invalid date range: To Date must be after From Date.")

    booking.price = int(sub.price) * days  # Final total price


    booking.save()
    return render(request, 'elder_bookings/booking_success.html', {
                'booking': booking,
                'days': days
            })
    
    
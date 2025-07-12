# Create your views here.
from django.shortcuts import render,redirect
from .forms import SubserviceForm,sub_services

def subservices_list(request):
    context={'subservices_list': sub_services.objects.all()}
    return render(request,"elder_subservices/subservice_list.html",context)

def subservices_add(request,id=0):
    if request.method=="GET":
        if id==0:
            form=SubserviceForm()
        else:
            sub=sub_services.objects.get(pk=id)
            form=SubserviceForm(instance=sub)
        return render(request,"elder_subservices/subservice_add.html",{'form':form})
    else:
        if id==0:
            form=SubserviceForm(request.POST,request.FILES)
        else:
            sub=sub_services.objects.get(pk=id)
            form=SubserviceForm(request.POST,request.FILES,instance=sub)

    if form.is_valid():
        form.save()
    return redirect('/subservices/list')

def subservices_delete(request,id):
    sub=sub_services.objects.get(pk=id)
    sub.delete()
    return redirect('/subservices/list')
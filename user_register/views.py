# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm,LoginForm
from elder_services.models import user_info

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect('home_page')  # Or 'home' if you want to go to the home page
# Signup view

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Saves uname and pwd to user_info table
            return redirect("login_page")
    else:
        form = SignupForm()

    return render(request, "registration/signup.html", {"form": form})

# Login view with cookie setting
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]


            user_qs = user_info.objects.filter(uname=uname, pwd=pwd)
            if user_qs.exists():
                user = user_qs.first()  # Take the first match if multiple exist
                request.session["user_id"] = user.id
                return redirect("get_service")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()


    return render(request, "registration/login.html", {"form": form})


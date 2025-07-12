from django.shortcuts import render,redirect
from django.http  import HttpResponse
def home_page(request):
    return render(request,"homepage.html")

def about_page(request):
    return render(request,"about.html")

def contact_page(request):
    return render(request,"contact.html")

def special_page(request):
    return render(request,"special.html")

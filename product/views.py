from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request, *arg, **kwargs):
    return render(request, "home.html", {})

def name_page(request, *arg, **kwargs):
    return render(request, "name.html", {})

def contact_page(request, *arg, **kwargs):
    return render(request, "contact.html", {})

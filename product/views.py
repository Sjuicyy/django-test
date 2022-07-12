from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(*args, **kwargs):
    return HttpResponse("<h1>this is home page<h1>")

def name_page(*args, **kwargs):
    return HttpResponse("<h1>this is name page<h1>")
    
def contact_page(*args, **kwargs):
    return HttpResponse("<h1>this is contact page<h1>")

def report_page(*args, **kwargs):
    return HttpResponse("<h1>this is report page<h1>")    
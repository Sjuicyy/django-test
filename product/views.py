from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(*args, **kwargs):
    return HttpResponse("<h1>this is homepage<h1>")

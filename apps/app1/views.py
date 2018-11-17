from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Here's a placeholder function!"
    return HttpResponse(response)

def home(request):
    return render(request,'app1/home.html')

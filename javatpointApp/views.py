from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def hello(request):
    return HttpResponse("<h2>Hello man</h2>")

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is%s  </h3></body></html>"%now
    return HttpResponse(html)
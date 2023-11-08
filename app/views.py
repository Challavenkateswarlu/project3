from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jam(request):
    return HttpResponse('<h1><marquee>hi how are you</h1></marquee>')
def ram(response):
    return HttpResponse('<h1><marquee>not interst</h1></marquee>')
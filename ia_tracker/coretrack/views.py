from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi, this is the IA Tracker!")

def coretr(request):
    return HttpResponse("Post-Login for Campaign")

# Create your views here.

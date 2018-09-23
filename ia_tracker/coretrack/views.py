from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi, this is the IA Tracker!")

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Portfolio home")

def contact(request):
    return HttpResponse("Contact Me: " + ""+ "Jarquevious Nelson 415) 990-3487")
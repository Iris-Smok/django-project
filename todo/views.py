"""
views.py
"""
from django.shortcuts import render, HttpResponse


# Create your views here.
def say_hello(request):
    """
    hello function
    """
    return HttpResponse("Hello!")

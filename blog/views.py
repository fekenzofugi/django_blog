from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = HttpResponse()
    response.content = "<h1>Blog Home</h1>"
    return response


def about(request):
    response = HttpResponse()
    response.content = "<h1>Blog About</h1>"
    return response

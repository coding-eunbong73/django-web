from django.shortcuts import render
from django.http.response import HttpResponse

def homepage(request):
    return HttpResponse("응 나야")

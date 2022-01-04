from django.shortcuts import render
from django.http.response import HttpResponse

def homepage(request):
    return render(request, "anyfile2.html")

from django.shortcuts import render
from django.http.response import HttpResponse
from .models import 아이디

def homepage(request):
    guests = 아이디.objects.all()
    context = { 
        "menu_name" : "짜장",
        "price" : "5000원",
        "guests" : guests
    }
    return render(request, "anyfile2.html", context)

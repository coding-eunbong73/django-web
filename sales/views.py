from django.shortcuts import render
from django.http.response import HttpResponse
from .models import 아이디, Sale

def homepage(request):
    guests = 아이디.objects.all()
    context = { 
        "menu_name" : "짜장",
        "price" : "5000원",
        "guests" : guests
    }
    return render(request, "anyfile2.html", context)

def salesList(request):
    saleGuests = Sale.objects.all()
    context = { 
        "saleGuests" : saleGuests
    }
    return render(request, "salesList.html", context)

def saleDetail(request, pk):
    print (pk)
    responseStr = "여기상세 정보입니다." + pk
    return HttpResponse(responseStr)

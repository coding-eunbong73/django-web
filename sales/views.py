from django.shortcuts import render
from django.http.response import HttpResponse
from .models import 아이디, Sale
from .forms import SaleForm

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
    sale = Sale.objects.get(id=pk)
    context = { 
        "sale" : sale
    }
    return render(request, "saleDetail.html", context)

def saleForm(request):
    print(request.POST)
    context = { 
        "saleForm" : SaleForm()
    }
    return render(request, "saleForm.html", context)    


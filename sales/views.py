from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import 아이디, Sale, Person
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
    
    if request.method == "POST":
        print ("포스트 메소드로 왔네요")
        form1 = SaleForm(request.POST)
        if form1.is_valid() :
            print( "유효하네요")
            print(form1.cleaned_data)
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            age = form1.cleaned_data['age']
            person = Person.objects.first()
            Sale.objects.create(
                first_name=first_name,
                last_name = last_name,
                age=age,
                person=person
            )
            print("세일이 입력되었습니다.")
            return redirect("/sales")

    context = { 
        "saleForm" : SaleForm()
    }
    return render(request, "saleForm.html", context)    


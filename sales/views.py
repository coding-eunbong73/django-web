from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from .models import 아이디, Sale, Person
from .forms import SaleForm, SaleModelForm
from django.views import generic

class homepageTemplateView(generic.TemplateView):
    template_name = "firstPage.html"

def homepage(request):
    return render(request, "firstPage.html")


class salesListView(generic.ListView):
    template_name = "folder/salesList.html"
    queryset = Sale.objects.all()
    context_object_name = "saleGuests"


def salesList(request):
    saleGuests = Sale.objects.all()
    context = { 
        "saleGuests" : saleGuests
    }
    return render(request, "folder/salesList.html", context)

class saleDetailView(generic.DetailView):
    template_name = "folder/saleDetail.html"
    queryset = Sale.objects.all()
    context_object_name = "sale"

   

def saleDetail(request, pk):
    sale = Sale.objects.get(id=pk)
    context = { 
        "sale" : sale
    }
    return render(request, "folder/saleDetail.html", context)

class saleFormView(generic.CreateView):
    template_name = "folder/saleForm.html"
    form_class = SaleModelForm

    def get_success_url(self):
        return reverse("sales:list")

def saleForm(request):
    print(request.POST)
    
    if request.method == "POST":
        form1 = SaleModelForm(request.POST)
        if form1.is_valid() :
            form1.save()
            return redirect("/sales")

    context = { 
        "saleForm" : SaleModelForm()
    }
    return render(request, "folder/saleForm.html", context)    

class saleUpdateView(generic.UpdateView):
    print("saleUpdateView!!!")

    template_name = "folder/saleUpdate.html"
    queryset = Sale.objects.all()

    form_class = SaleModelForm
    context_object_name = "sale"

    def get_success_url(self):
        return reverse("sales:list")

def saleUpdate(request, pk):
    print("saleUpdate!!!")
    sale = Sale.objects.get(id=pk)
    form1 = SaleModelForm(instance=sale)
    if request.method == "POST":
        form1 = SaleModelForm(request.POST, instance=sale)
        if form1.is_valid() :
            form1.save()

            return redirect("/sales")   
 
    context = { 
        "saleForm" : form1,
        "sale": sale
    }
    return render(request, "folder/saleUpdate.html", context)

class saleDeleteView(generic.DeleteView):
    print("saleDeleteView!!!")
    queryset = Sale.objects.all()
    template_name = "folder/saleDelete.html"


    def get_success_url(self):
        return reverse("sales:list")

def saleDelete(request, pk):
    print("test")
    sale = Sale.objects.get(id=pk)
    sale.delete()
    return redirect("/sales")   


""" def saleUpdate(request, pk):
    sale = Sale.objects.get(id=pk)
    form1 = SaleForm()
    if request.method == "POST":
        form1 = SaleForm(request.POST)
        if form1.is_valid() :
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            age = form1.cleaned_data['age']

            sale.first_name = first_name
            sale.last_name  = last_name 
            sale.age = age 
            sale.save()

            return redirect("/sales")   
 
    context = { 
        "sale" : sale,
        "saleForm" : form1
    }
    return render(request, "saleUpdate.html", context) """


""" def saleForm(request):
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
    return render(request, "saleForm.html", context)     """


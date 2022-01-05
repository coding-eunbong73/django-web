from django.urls import path
from .views import homepage
from .views import salesList, saleDetail, saleForm, saleUpdate

app_name = "homepage"

urlpatterns = [
    #path ('', homepage),
    path ('', salesList),
    path ('make/', saleForm),
    path ('<int:pk>/', saleDetail),
    path ('<int:pk>/update', saleUpdate),
]
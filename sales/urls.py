from django.urls import path
from .views import homepage
from .views import salesList, saleDetail, saleForm, saleUpdate, saleDelete

app_name = "sales"

urlpatterns = [
    #path ('', homepage),
    path ('', salesList, name='list'),
    path ('make/', saleForm, name='create'),
    path ('<int:pk>/', saleDetail, name='detail'),
    path ('<int:pk>/update', saleUpdate, name='update'),
    path ('<int:pk>/delete', saleDelete, name='delete'),
]
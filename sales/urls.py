from django.urls import path
from .views import homepage
from .views import salesList, saleDetail, saleForm, saleUpdate, saleDelete, saleFormView, salesListView, saleDetailView, saleUpdateView, saleDeleteView

app_name = "sales"

urlpatterns = [
    #path ('', homepage),


    #path ('', salesList, name='list'),
    path ('', salesListView.as_view(), name='list'),

    #path ('make/', saleForm, name='create'),
    path ('make/', saleFormView.as_view(), name='create'),

    #path ('<int:pk>/', saleDetail, name='detail'),
    path ('<int:pk>/detail', saleDetailView.as_view(), name='detail'),


    #path ('<int:pk>/update', saleUpdate, name='update'),
    path ('<int:pk>/update', saleUpdateView.as_view(), name='update'),


    #path ('<int:pk>/delete', saleDelete, name='delete'),
    path ('<int:pk>/delete', saleDeleteView.as_view(), name='delete'),
]
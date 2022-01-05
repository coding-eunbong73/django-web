from django.urls import path
from .views import homepage
from .views import salesList, saleDetail

app_name = "homepage"

urlpatterns = [
    path ('', homepage),
    path ('sales', salesList),
    path ('sales/<pk>', saleDetail)
]
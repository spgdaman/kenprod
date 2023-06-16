from django.urls import path
from .views import get_market_price, export_csv, search, ProductsUploadView

urlpatterns = [
    path('', get_market_price, name='home'),
    path('export/export_csv/', export_csv, name='export_csv'),
    path('search/', search, name="search"),
    path('importproducts/', ProductsUploadView.as_view(), name='importproducts')
]
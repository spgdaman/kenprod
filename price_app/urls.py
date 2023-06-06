from django.urls import path
from .views import get_market_price, export_csv

urlpatterns = [
    path('', get_market_price, name='home'),
    path('export/csv-database-write/', export_csv, name='csv_database_write'),
]
from django.urls import path
from .views import get_market_price, export_csv, search, global_search, ProductsUploadView, CustomerUploadView,CustomerBranchesUploadView

urlpatterns = [
    path('', get_market_price, name='home'),
    path('export/export_csv/', export_csv, name='export_csv'),
    path('search/', search, name="search"),
    path('global_search/', global_search, name="global_search"),
    path('import_products/', ProductsUploadView.as_view(), name='import_products'),
    path('import_customers/', CustomerUploadView.as_view(), name='import_customers'),
    path('import_customer_branches/', CustomerBranchesUploadView.as_view(), name='import_customer_branches')
]
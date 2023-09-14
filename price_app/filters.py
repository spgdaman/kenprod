from .models import MarketPrice
import django_filters
from django import forms

class MarketPriceFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    sales_person = django_filters.CharFilter(lookup_expr='icontains')
    customer_name = django_filters.CharFilter(lookup_expr='icontains')
    customer_branch = django_filters.CharFilter(lookup_expr='icontains')
    kenpoly_product_name = django_filters.CharFilter(lookup_expr='icontains')
    competitor_name = django_filters.CharFilter(lookup_expr='icontains')
    competitor_product_name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = MarketPrice
        fields = ['sales_person', 'customer_name', 'customer_branch', 'kenpoly_product_name', 'competitor_name', 'competitor_product_name', 'created_at']
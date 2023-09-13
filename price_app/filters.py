from .models import MarketPrice
import django_filters
from django import forms

class MarketPriceFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter(
        # lookup_expr='icontains',
        # widget= forms.DateInput(
        #     attrs={
        #         'class': 'datepicker'
        #     }
        # )
    )
    # created_at_gt = django_filters.DateFromToRangeFilter(field_name='created_at', lookup_expr='gt')
    # created_at_lt = django_filters.DateFromToRangeFilter(field_name='created_at', lookup_expr='lt')
    class Meta:
        model = MarketPrice
        fields = ['sales_person', 'customer_name', 'customer_branch', 'kenpoly_product_name', 'competitor_name', 'competitor_product_name', 'created_at']
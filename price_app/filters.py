from .models import MarketPrice
import django_filters

class MarketPriceFilter(django_filters.FilterSet):
    class Meta:
        model = MarketPrice
        fields = ['sales_person', 'customer_name', 'customer_branch', 'kenpoly_product_name', 'competitor_name', 'competitor_product_name', 'created_at']
from django.urls import path
from .views import get_market_price

urlpatterns = [
    path('', get_market_price, name='home')
]
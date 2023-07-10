from django.urls import path
from .views import labour_input_fg, labour_input_sfg

urlpatterns = [
    path("labour_input_finsihed_goods/", labour_input_fg, name='labour_input_fg'),
    path("labour_input_semifinsihed_goods/", labour_input_sfg, name='labour_input_sfg'),
]
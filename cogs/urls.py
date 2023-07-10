from django.urls import path
from .views import labour_input_fg, labour_input_sfg, power_input_fg, power_input_sfg, packing_input_fg, packing_input_sfg, label_input_fg, label_input_sfg, foiling_input_fg, foiling_input_sfg

urlpatterns = [
    path("labour_input_finsihed_goods/", labour_input_fg, name='labour_input_fg'),
    path("labour_input_semifinsihed_goods/", labour_input_sfg, name='labour_input_sfg'),
    
    path("power_input_finsihed_goods/", power_input_fg, name='power_input_fg'),
    path("power_input_semifinsihed_goods/", power_input_sfg, name='power_input_sfg'),

    path("packing_input_finsihed_goods/", packing_input_fg, name='packing_input_fg'),
    path("packing_input_semifinsihed_goods/", packing_input_sfg, name='packing_input_sfg'),

    path("label_input_finsihed_goods/", label_input_fg, name='label_input_fg'),
    path("label_input_semifinsihed_goods/", label_input_sfg, name='label_input_sfg'),

    path("foiling_input_finsihed_goods/", foiling_input_fg, name='foiling_input_fg'),
    path("foiling_input_semifinsihed_goods/", foiling_input_sfg, name='foiling_input_sfg'),
]
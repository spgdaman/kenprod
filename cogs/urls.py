from django.urls import path
from . import views

urlpatterns = [
    path("labour_input_finished_goods/", views.labour_input_fg, name='labour_input_fg'),
    path("labour_input_semifinsihed_goods/", views.labour_input_sfg, name='labour_input_sfg'),

    path("power_input_finished_goods/", views.power_input_fg, name='power_input_fg'),
    path("power_input_semifinsihed_goods/", views.power_input_sfg, name='power_input_sfg'),

    path("packing_input_finished_goods/", views.packing_input_fg, name='packing_input_fg'),
    path("packing_input_semifinsihed_goods/", views.packing_input_sfg, name='packing_input_sfg'),

    path("label_input_finished_goods/", views.label_input_fg, name='label_input_fg'),
    path("label_input_semifinsihed_goods/", views.label_input_sfg, name='label_input_sfg'),

    path("foiling_input_finished_goods/", views.foiling_input_fg, name='foiling_input_fg'),
    path("foiling_input_semifinsihed_goods/", views.foiling_input_sfg, name='foiling_input_sfg'),

    path("finished_goods_input/", views.finished_good_input, name="finished_good_input"),

    path("semi_finished_goods_input/", views.semi_finished_good_input, name="semi_finished_good_input"),

    path("raw_material_category_input/", views.raw_material_category_input, name="raw_material_category_input"),
    path("raw_material_line_item_input/", views.raw_material_line_item_input, name="raw_material_category_line_item_input"),
    path("raw_material_finished_goods_input/", views.raw_material_finished_goods_input, name="raw_material_finished_goods_input"),
    path("raw_material_semi_finished_goods_input/", views.raw_material_semi_finished_goods_input, name="raw_material_semi_finished_goods_input"),

    path("external_component_name_input/", views.external_component_name_input, name="external_component_name_input"),
    path("external_component_line_item_input/", views.external_component_line_item_input, name="external_component_line_item_input"),
    path("external_component_finished_goods_input/", views.external_component_finished_goods_input, name="external_component_finished_goods_input"),
    path("external_component_semi_finished_goods_input/", views.external_component_semi_finished_goods_input, name="external_component_semi_finished_goods_input"),
]
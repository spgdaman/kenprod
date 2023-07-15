from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name='welcome'),
    path("listings/", views.listings, name='listings'),

    path("labour_input_finished_goods/", views.labour_input_fg, name='labour_input_fg'),
    path("labour_input_semifinsihed_goods/", views.labour_input_sfg, name='labour_input_sfg'),
    path("labour_cost_finished_goods_listing/", views.labour_fg_listing, name="labour_fg_listing"),
    path("labour_cost_semi_finished_goods_listing/", views.labour_sfg_listing, name="labour_sfg_listing"),

    path("power_input_finished_goods/", views.power_input_fg, name='power_input_fg'),
    path("power_input_semifinished_goods/", views.power_input_sfg, name='power_input_sfg'),
    path("power_cost_finished_goods_listing/", views.power_fg_listing, name="power_fg_listing"),
    path("power_cost_semi_finished_goods_listing/", views.power_sfg_listing, name="power_sfg_listing"),

    path("packing_input_finished_goods/", views.packing_input_fg, name='packing_input_fg'),
    path("packing_input_semifinished_goods/", views.packing_input_sfg, name='packing_input_sfg'),
    path("packing_cost_finished_goods_listing/", views.packing_fg_listing, name="packing_fg_listing"),
    path("packing_cost_semi_finished_goods_listing/", views.packing_sfg_listing, name="packing_sfg_listing"),
    
    path("label_input_finished_goods/", views.label_input_fg, name='label_input_fg'),
    path("label_input_semifinished_goods/", views.label_input_sfg, name='label_input_sfg'),
    path("label_cost_finished_goods_listing/", views.label_fg_listing, name='label_fg_listing'),
    path("label_cost_semi_finished_goods_listing/", views.label_sfg_listing, name='label_sfg_listing'),

    path("foiling_input_finished_goods/", views.foiling_input_fg, name='foiling_input_fg'),
    path("foiling_input_semifinished_goods/", views.foiling_input_sfg, name='foiling_input_sfg'),
    path("foiling_cost_finished_goods_listing/", views.foiling_fg_listing, name='foiling_fg_listing'),
    path("foiling_cost_semi_finished_goods_listing/", views.foiling_sfg_listing, name='foiling_sfg_listing'),

    path("finished_goods_input/", views.finished_good_input, name="finished_good_input"),
    path("finished_goods_listing/", views.fg_listing, name='fg_listing'),

    path("semi_finished_goods_input/", views.semi_finished_good_input, name="semi_finished_good_input"),
    path("semi_finished_goods_listing/", views.sfg_listing, name='sfg_listing'),

    path("raw_material_category_input/", views.raw_material_category_input, name="raw_material_category_input"),
    path("raw_material_line_item_input/", views.raw_material_line_item_input, name="raw_material_category_line_item_input"),
    path("raw_material_finished_goods_input/", views.raw_material_finished_goods_input, name="raw_material_finished_goods_input"),
    path("raw_material_semi_finished_goods_input/", views.raw_material_semi_finished_goods_input, name="raw_material_semi_finished_goods_input"),
    path("raw_materials_finished_goods_listing/", views.rm_fg_listing, name='rm_fg_listing'),
    path("raw_materials_semi_finished_goods_listing/", views.rm_sfg_listing, name='rm_sfg_listing'),
    path("raw_materials_name_listing/", views.rm_name_listing, name='rm_name_listing'),
    path("raw_materials_line_item_listing/", views.rm_line_item_listing, name='rm_line_item_listing'),

    path("external_component_name_input/", views.external_component_name_input, name="external_component_name_input"),
    path("external_component_line_item_input/", views.external_component_line_item_input, name="external_component_line_item_input"),
    path("external_component_finished_goods_input/", views.external_component_finished_goods_input, name="external_component_finished_goods_input"),
    path("external_component_semi_finished_goods_input/", views.external_component_semi_finished_goods_input, name="external_component_semi_finished_goods_input"),
    path("external_component_finished_goods_listing/", views.ec_fg_listing, name='ec_fg_listing'),
    path("external_component_semi_finished_goods_listing/", views.ec_sfg_listing, name='ec_sfg_listing'),
    path("external_component_name_listing/", views.ec_name_listing, name='ec_name_listing'),
    path("external_component_line_item_listing/", views.ec_line_item_listing, name='ec_line_item_listing'),
]
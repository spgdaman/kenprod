from django.contrib import admin
from . import models

admin.site.register(models.ExchangeRate)
admin.site.register(models.Labeling)

class FinishedGoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'primary_sales_channel', 'weight', 'created_at']
    search_fields = ("name",)
    list_filter = ("name", )
admin.site.register(models.FinishedGood, FinishedGoodAdmin)

class SemiFinishedGoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'fg_name', 'weight', 'component_quantity', 'composition', 'price_for_composition_per_kg', 'material_cost_per_unit','created_at']
    search_fields = ("name", )
admin.site.register(models.SemiFinishedGood, SemiFinishedGoodAdmin)

admin.site.register(models.Foiling)

class PackingAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'sa_label', 'paper_label', 'woven_bag', 'carton', 'foils', 'inner_bag', 'woven_tubing', 'strapping', 'kes_u', 'created_at']
    list_filter = ("fg_name", )
admin.site.register(models.Packing, PackingAdmin)

class PowerAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'sfg_name', 'component', 'mould', 'mmts', 'kwh', 'kes_kw', 'kes_hr', 'ct', 'cavity', 'u_h', 'kes_u', 'kes_sfg', 'created_at']
    list_filter = ("fg_name", )
admin.site.register(models.Power, PowerAdmin)

class LabourCostAdmin(admin.ModelAdmin):
    list_display = ['effective_from', 'effective_to', 'cost']
admin.site.register(models.LabourCost)

class LabourAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'sfg_name', 'component', 'mould', 'mac_fte']
admin.site.register(models.Labour)

class RawMaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ['material_name', 'created_at']
    search_fields = ("material_name",)
    list_filter = ("material_name", )
admin.site.register(models.RawMaterialCategory, RawMaterialCategoryAdmin)

class RawMaterialLineItemAdmin(admin.ModelAdmin):
    list_display = ['material_name', 'raw_material_cost', 'landing_cost_percentage', 'landed_cost_per_kg', 'cost_per_kg', 'created_at' ]
    search_fields = ("material_name",)
admin.site.register(models.RawMaterialLineItem, RawMaterialLineItemAdmin)

class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'sfg_name', 'raw_material', 'created_at']
admin.site.register(models.RawMaterial)

class ExternalComponentNameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ("name",)
    list_filter = ("name", )
admin.site.register(models.ExternalComponentName, ExternalComponentNameAdmin)

class ExternalComponentLineItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'price_per_unit', 'cost']
    search_fields = ("name",)
    list_filter = ("name", )
admin.site.register(models.ExternalComponentLineItem, ExternalComponentLineItemAdmin)

class ExternalComponentAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'component', 'created_at']
    list_filter = ("fg_name", )
admin.site.register(models.ExternalComponent, ExternalComponentAdmin)

class MouldNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    search_fields = ("name",)
admin.site.register(models.MouldName, MouldNameAdmin)

class MouldAdmin(admin.ModelAdmin):
    list_display = ['name', 'fg_name', 'sfg_name', 'group', 'work_center', 'cavity_number', 'maximum_capacity', 'optimum_capacity', 'cycle_time']
    search_fields = ("name",)
admin.site.register(models.Mould, MouldAdmin)
# admin.site.register(models.Machine)

class SalesPriceAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'psc_price', 'ws_price', 'markup']
    list_filter = ("fg_name", )  
admin.site.register(models.SalesPrice, SalesPriceAdmin)

class CompositionNameAdmin(admin.ModelAdmin):
    list_display = ['composition_name']
    search_fields = ("composition_name",)
admin.site.register(models.CompositionName, CompositionNameAdmin)

class CompositionAdmin(admin.ModelAdmin):
    list_display = ['composition', 'material_name', 'ratio', 'price_per_kg', 'price_for_ratio']
    # list_display = [field.name for field in models.Composition._meta.get_fields()]
    search_fields = ("composition", "material_name",)
    list_filter = ("composition", "material_name",)      
admin.site.register(models.Composition, CompositionAdmin)

class ChangeOverTimeAdmin(admin.ModelAdmin):
    list_display = ['co_time', 'hrs']
admin.site.register(models.ChangeOverTime, ChangeOverTimeAdmin)

class ChangeOverAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.ChangeOver._meta.get_fields()]
admin.site.register(models.ChangeOver, ChangeOverAdmin)

class PrintAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Print._meta.get_fields()]
admin.site.register(models.Print, PrintAdmin)
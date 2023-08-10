from django.contrib import admin
from . import models

admin.site.register(models.ExchangeRate)
admin.site.register(models.Labeling)
admin.site.register(models.RawMaterial)
admin.site.register(models.RawMaterialLineItem)
admin.site.register(models.FinishedGood)
admin.site.register(models.SemiFinishedGood)
admin.site.register(models.Foiling)
admin.site.register(models.Packing)
admin.site.register(models.Power)
admin.site.register(models.Labour)
admin.site.register(models.RawMaterialCategory)
admin.site.register(models.ExternalComponentName)
admin.site.register(models.ExternalComponentLineItem)
admin.site.register(models.ExternalComponent)



class MouldNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
admin.site.register(models.MouldName, MouldNameAdmin)

class MouldAdmin(admin.ModelAdmin):
    list_display = ['name', 'fg_name', 'sfg_name', 'group', 'work_center', 'cavity_number', 'maximum_capacity', 'optimum_capacity', 'cycle_time']
admin.site.register(models.Mould, MouldAdmin)
# admin.site.register(models.Machine)

class SalesPriceAdmin(admin.ModelAdmin):
    list_display = ['fg_name', 'psc_price', 'ws_price', 'markup']
admin.site.register(models.SalesPrice, SalesPriceAdmin)

class CompositionNameAdmin(admin.ModelAdmin):
    list_display = ['composition_name']
admin.site.register(models.CompositionName, CompositionNameAdmin)

class CompositionAdmin(admin.ModelAdmin):
    list_display = ['composition', 'material_name', 'ratio', 'price_per_kg', 'price_for_ratio']
    # list_display = [field.name for field in models.Composition._meta.get_fields()]
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
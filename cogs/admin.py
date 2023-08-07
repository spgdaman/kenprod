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
admin.site.register(models.ExternalComponent)
admin.site.register(models.ExternalComponentLineItem)
admin.site.register(models.ExternalComponentName)
admin.site.register(models.Mould)
# admin.site.register(models.Machine)
admin.site.register(models.SalesPrice)
admin.site.register(models.Composition)
admin.site.register(models.ChangeOver)
admin.site.register(models.ChangeOverTime)
admin.site.register(models.Print)
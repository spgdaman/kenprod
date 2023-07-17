from django.contrib import admin
from .models import ExchangeRate,Labeling,RawMaterial,RawMaterialLineItem,RawMaterialCategory,FinishedGood,SemiFinishedGood,Foiling,Packing,Power,Labour,ExternalComponent,ExternalComponentLineItem,ExternalComponentName

admin.site.register(ExchangeRate)
admin.site.register(Labeling)
admin.site.register(RawMaterial)
admin.site.register(RawMaterialLineItem)
admin.site.register(FinishedGood)
admin.site.register(SemiFinishedGood)
admin.site.register(Foiling)
admin.site.register(Packing)
admin.site.register(Power)
admin.site.register(Labour)
admin.site.register(RawMaterialCategory)
admin.site.register(ExternalComponent)
admin.site.register(ExternalComponentLineItem)
admin.site.register(ExternalComponentName)
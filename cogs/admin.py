from django.contrib import admin
# from .models import FinishedGood, Composition, RawMaterial,VariableCost,Packing,
from .models import (
    Test, 
    FinishedGood, 
    Composition, 
    CompositionLineItem,
    RawMaterialLineItem,
    RawMaterial,
    RawMaterialCategory,
    Attribute,
    Recipe,
)

admin.site.register(FinishedGood)
admin.site.register(Composition)
admin.site.register(CompositionLineItem)
admin.site.register(RawMaterialLineItem)
admin.site.register(RawMaterial)
admin.site.register(RawMaterialCategory)
admin.site.register(Attribute)
admin.site.register(Recipe)
# admin.site.register(VariableCost)
# admin.site.register(Packing)
admin.site.register(Test)
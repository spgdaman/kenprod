from django.contrib import admin
from .models import FinishedGood, Composition, RawMaterial,VariableCost,Packing

admin.site.register(FinishedGood)
admin.site.register(Composition)
admin.site.register(RawMaterial)
admin.site.register(VariableCost)
admin.site.register(Packing)
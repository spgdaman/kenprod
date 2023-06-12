from django.contrib import admin
from .models import FinishedGoods, Composition, RawMaterials

admin.site.register(FinishedGoods)
admin.site.register(Composition)
admin.site.register(RawMaterials)
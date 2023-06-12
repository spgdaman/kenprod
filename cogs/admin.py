from django.contrib import admin
from .models import FinishedGood, Composition, RawMaterial

admin.site.register(FinishedGood)
admin.site.register(Composition)
admin.site.register(RawMaterial)
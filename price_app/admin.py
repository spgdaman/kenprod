from django.contrib import admin
from .models import MarketPrice,Products,Customers,CustomerBranches

admin.site.register(MarketPrice)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(CustomerBranches)
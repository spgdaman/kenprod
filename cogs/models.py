from django.db import models
from django.conf import settings

class FinishedGoods(models.Model):
    name = models.CharField(max_length=50, blank=True)
    attribute = models.CharField(max_length=30, blank=True)
    weight = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    recipe = models.CharField(max_length=50, blank=True)
    selling_price = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()

class Composition(models.Model):
    item_name = models.ForeignKey(FinishedGoods, on_delete=models.CASCADE)
    composition = models.CharField(max_length=30, blank=True)
    ratio = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    price_per_kg = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()

    def get_price_for_ratio(self):
        '''returns the price for ratio'''
        if self.ratio < 0:
            return (self.price_per_kg * (-1*self.ratio)) * 100
        else:
            return (self.price_per_kg * self.ratio) * 100
    price_for_ratio = property(get_price_for_ratio)

class RawMaterials(models.Model):
    item_name = models.ForeignKey(FinishedGoods, on_delete=models.CASCADE)
    material = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    rm_cost = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    landing_cost = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    
    def landed_cost_per_kilo(self):
        '''returns the landing cost per kg'''
        if self.rm_cost < 0:
            return (-1*self.rm_cost)*(1+(self.landing_cost/100))
        else:
            return self.rm_cost *(1+(self.landing_cost/100))
        
    landed_cost_per_kg = property(landed_cost_per_kilo)

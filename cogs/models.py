from django.db import models
from django.conf import settings

class FinishedGood(models.Model):
    name = models.CharField(max_length=50, blank=True)
    attribute = models.CharField(max_length=30, blank=True)
    weight = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    recipe = models.CharField(max_length=50, blank=True)
    selling_price = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()

class Composition(models.Model):
    item_name = models.ForeignKey(FinishedGood, on_delete=models.CASCADE)
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

class RawMaterial(models.Model):
    item_name = models.ForeignKey(FinishedGood, on_delete=models.CASCADE)
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

class VariableCost(models.Model):
    item_name = models.ForeignKey(FinishedGood, on_delete=models.CASCADE)
    weight_polymers_kilo = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    power = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    labour = models.DecimalField(blank=True, max_digits=10, decimal_places=2)

class Packing(models.Model):
    PACKING_UNIT = [("pcs", "Pieces"),
                    ("pc", "Piece"),
                    ("doz", "Dozen"),
                    ("set", "Set"),
                    ]
    item_name = models.ForeignKey(FinishedGood, on_delete=models.CASCADE)
    pack_unit = models.CharField(max_length=10, choices=PACKING_UNIT, default="pcs")
    pack_size = models.IntegerField()
    no_of_components = models.IntegerField()
    cost_of_woven   = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    cost_of_pp_woven = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    carton = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    cost_of_inner_bag = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    label_pcs = models.IntegerField()
    labels_per_pack_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    carton_label = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    printing = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    strapping = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    pipe = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    bottle = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    cap = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    sleeves = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    glue = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    shrink_wrap = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    foil = models.DecimalField(blank=True, max_digits=10, decimal_places=2)

    def total_cost_of_packing(self):
        variable_costs = (
            self.cost_of_woven,
            self.cost_of_pp_woven,
            self.carton,
            self.cost_of_inner_bag,
            self.carton_label,
            self.printing,
            self.strapping,
            self.pipe,
            self.bottle,
            self.cap,
            self.sleeves,
            self.glue,
            self.shrink_wrap,
            self.foil)
        return sum(variable_costs)
    total_packaging_cost = property(total_cost_of_packing)
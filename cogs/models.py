from django.db import models
from django.conf import settings

class ExchangeRate(models.Model):
    rate = models.DecimalField(blank=True, max_digits=10, decimal_places=4)
    
    def __str__(self):
        return f"{self.rate}"
    
class Mould(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=50, blank=False)
    mould = models.ForeignKey(Mould, models.DO_NOTHING, blank=False, null=False)

    def __str__(self):
        return self.name

class FinishedGood(models.Model):
    name = models.CharField(max_length=50, blank=True)
    unit = models.DecimalField(blank=True, max_digits=50, decimal_places=4)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=4)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class SemiFinishedGood(models.Model):
    name = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    unit = models.DecimalField(blank=True, max_digits=50, decimal_places=4)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class RawMaterialCategory(models.Model):
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class RawMaterialLineItem(models.Model):
    name = models.ForeignKey(RawMaterialCategory, models.DO_NOTHING, blank=True, null=True)
    unit = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.category

class RawMaterial(models.Model):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    raw_material = models.ForeignKey(RawMaterialLineItem, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.fg_name == None:
            return f"{self.raw_material} material used for --> product {self.sfg_name}"
        else:
            return f"{self.raw_material} material used for --> product {self.fg_name}"
    
class ExternalComponentName(models.Model):
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ExternalComponentLineItem(models.Model):
    name = models.ForeignKey(ExternalComponentName, models.DO_NOTHING, blank=True, null=True)
    unit = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.name
    
class ExternalComponent(models.Model):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    component = models.ForeignKey(ExternalComponentLineItem, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.component.name}"

class Labeling(models.Model):
    description = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    unit = models.IntegerField(null=True, blank=True)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
class Foiling(models.Model):
    description = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    unit = models.IntegerField(null=True, blank=True)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
class Packing(models.Model):
    description = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    unit = models.IntegerField(null=True, blank=True)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Power(models.Model):
    description = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    unit = models.IntegerField(null=True, blank=True)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=False, null=False)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
class Labour(models.Model):
    description = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    unit = models.IntegerField(null=True, blank=True)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    

# class Attribute(models.Model):
#     attribute_name = models.CharField(max_length=30, blank=True)

#     def __str__(self):
#         return self.attribute_name

# class Recipe(models.Model):
#     recipe_name = models.CharField(max_length=30, blank=True)

#     def __str__(self):
#         return self.recipe_name

# class FinishedGood(models.Model):
#     name = models.CharField(max_length=50, blank=True)
#     attribute = models.ForeignKey(Attribute, models.DO_NOTHING, blank=True, null=True)
#     weight = models.DecimalField(blank=True, max_digits=50, decimal_places=4)
#     recipe = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)
#     selling_price = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.name

# class RawMaterialCategory(models.Model):
#     category = models.CharField(max_length=50, blank=True)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.category

# class RawMaterialLineItem(models.Model):
#     # item_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
#     material = models.CharField(max_length=50, blank=True)
#     category = models.ForeignKey(RawMaterialCategory, models.DO_NOTHING, blank=True, null=True)
#     rm_cost = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
#     landing_cost = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(null=True, blank=True)
    
#     def landed_cost_per_kilo(self):
#         '''returns the landing cost per kg'''
#         if self.rm_cost < 0:
#             return (-1*self.rm_cost)*(1+(self.landing_cost/100))
#         else:
#             return self.rm_cost *(1+(self.landing_cost/100))
        
#     landed_cost_per_kg = property(landed_cost_per_kilo)

#     def __str__(self):
#         return self.material

# class RawMaterial(models.Model):
#     item_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
#     raw_material = models.ForeignKey(RawMaterialLineItem, models.DO_NOTHING, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.raw_material} material used for --> product {self.item_name}"

# class CompositionLineItem(models.Model):
#     composite_material = models.CharField(max_length=30, blank=True)

#     def __str__(self):
#         return self.composite_material

# class Composition(models.Model):
#     item_name = models.ForeignKey(RawMaterial, models.DO_NOTHING, blank=True, null=True)
#     composition = models.ForeignKey(CompositionLineItem, models.DO_NOTHING, blank=True, null=True)
#     ratio = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
#     price_per_kg = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.composition} composition for --> {self.item_name}"

#     def get_price_for_ratio(self):
#         '''returns the price for ratio'''
#         if self.ratio < 0:
#             return (self.price_per_kg * (-1*self.ratio)) * 100
#         else:
#             return (self.price_per_kg * self.ratio) * 100
#     price_for_ratio = property(get_price_for_ratio)

# class SemiFinishedGood(models.Model):
#     item_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
#     sfg_name = models.CharField(max_length=50, blank=True)
#     weight = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     attribute = models.ForeignKey(Attribute, models.DO_NOTHING, blank=True, null=True)
#     component_quantity = models.IntegerField()
#     composition = models.ForeignKey(Composition, models.DO_NOTHING, blank=True, null=True)
#     # recipe = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)


# class ExternalComponent(models.Model):
#     pass

# class Packaging(models.Model):
#     pass

# class VariableCost(models.Model):
#     # item_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
#     weight_polymers_kilo = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     power = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     labour = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField()

# class Packing(models.Model):
#     PACKING_UNIT = [
#                     ("doz", "Dozen"),
#                     ("pc", "Piece"),
#                     ("pcs", "Pieces"),
#                     ("set", "Set"),
#                     ]
#     # item_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
#     pack_unit = models.CharField(max_length=10, choices=PACKING_UNIT, default="pcs")
#     pack_size = models.IntegerField()
#     no_of_components = models.IntegerField()
#     cost_of_woven   = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     cost_of_pp_woven = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     carton = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     cost_of_inner_bag = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     label_pcs = models.IntegerField()
#     labels_per_pack_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     carton_label = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     printing = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     strapping = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     pipe = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     bottle = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     cap = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     sleeves = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     glue = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     shrink_wrap = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
#     foil = models.DecimalField(blank=True, max_digits=10, decimal_places=2)

#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField()

#     def total_cost_of_packing(self):
#         variable_costs = (
#             self.cost_of_woven,
#             self.cost_of_pp_woven,
#             self.carton,
#             self.cost_of_inner_bag,
#             self.carton_label,
#             self.printing,
#             self.strapping,
#             self.pipe,
#             self.bottle,
#             self.cap,
#             self.sleeves,
#             self.glue,
#             self.shrink_wrap,
#             self.foil)
#         return sum(variable_costs)
#     total_packaging_cost = property(total_cost_of_packing)

class Test(models.Model):
    name = models.CharField(max_length=50, blank=True)
    attribute = models.CharField(max_length=30, blank=True)
    weight = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    recipe = models.CharField(max_length=50, blank=True)
    selling_price = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank = True)
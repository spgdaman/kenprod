from django.db import models
from django.conf import settings
from computedfields.models import ComputedFieldsModel, computed, compute

class ExchangeRate(models.Model):
    effective_from = models.DateField()
    effective_to = models.DateField()
    rate = models.DecimalField(blank=True, max_digits=10, decimal_places=4)

class ChangeOverTime(models.Model):
    co_time = models.IntegerField(null=True, blank=True)
    hrs = models.DecimalField(blank=True, max_digits=10, decimal_places=5)

# class Machine(models.Model):
#     name = models.CharField(max_length=50, blank=False)
#     mould = models.ForeignKey(Mould, models.DO_NOTHING, blank=False, null=False)

#     def __str__(self):
#         return self.name

class FinishedGood(models.Model):
    name = models.CharField(max_length=50, blank=True)
    primary_sales_channel = models.CharField(max_length=20, blank=True)
    weight = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=4)
    # unit = models.DecimalField(blank=True, max_digits=50, decimal_places=4)
    # cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=4)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class SemiFinishedGood(models.Model):
    name = models.CharField(max_length=50, blank=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    weight = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=4)
    component_quantity = models.IntegerField(blank=True, null=True)
    # cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class MouldName(models.Model):
    name = models.CharField(max_length=50, blank=False)
    group = models.CharField(max_length=50, blank=False)
    
class Mould(models.Model):
    co_time = models.ForeignKey(ChangeOverTime, models.DO_NOTHING, blank=True, null=True)
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    name = models.ForeignKey(MouldName, models.DO_NOTHING, blank=True, null=True)
    group = models.CharField(max_length=50, blank=True)
    work_center = models.CharField(max_length=50, blank=True)
    cavity_number = models.IntegerField(null=True)
    maximum_capacity = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    optimum_capacity = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    cycle_time = models.IntegerField(null=True)
    # u_h = models.IntegerField(null=True)

    def __str__(self):
        if type(self.sfg_name) == None:
            return f"{self.name} for {self.sfg_name.name} Semi Finished Goods"
        elif type(self.fg_name) != None:
            return f"{self.name} for {self.fg_name} Finished Goods"
    
    # def get_computed(self):
    #     result = (self.cavity_number * 60 * 60) / self.cycle_time

    # def save(self, *args, **kwargs):
    #     self.u_h = self.get_computed()
    #     super(Mould, self).save(*args, **kwargs)
    
class SalesPrice(models.Model):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=False, null=False)
    psc_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    ws_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    markup = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sales Price"

    def __str__(self):
        return f"Selling Price for {self.fg_name}"
    
class RawMaterialCategory(models.Model):
    material_name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_name

class RawMaterialLineItem(ComputedFieldsModel):
    material_name = models.ForeignKey(RawMaterialCategory, models.DO_NOTHING, blank=True, null=True)
    raw_material_cost = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    landing_cost_percentage = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

    @computed(models.DecimalField(blank=True, max_digits=5, decimal_places=2))
    def landed_cost_per_kg(self):
        return (1 + self.landing_cost_percentage) * self.raw_material_cost
    cost_per_kg = models.DecimalField(blank=True, max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_name.material_name

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
    
class ExternalComponentLineItem(ComputedFieldsModel):
    name = models.ForeignKey(ExternalComponentName, models.DO_NOTHING, blank=True, null=True)
    unit = models.DecimalField(blank=True, max_digits=50, decimal_places=2)
    price_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2) 
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.name
    
    @computed(models.DecimalField(blank=True, max_digits=10, decimal_places=2))
    def cost(self):
        return self.unit * self.price_per_unit
    
    # def get_computed(self):
    #     result = self.unit * self.price_per_unit

    # def save(self, *args, **kwargs):
    #     self.cost = self.get_computed()
    #     super(Mould, self).save(*args, **kwargs)
    
class ExternalComponent(models.Model):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
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

class Power(ComputedFieldsModel):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    component = models.IntegerField(null=True, blank=True)
    mould = models.ForeignKey(Mould, models.DO_NOTHING, blank=False, null=True)
    # cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=False, null=True)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fg_name} {self.sfg_name}"
    
    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['work_center'])])
    def mmts(self):
        return self.mould.work_center
    
    @computed(models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2), depends=[('mould', ['work_center'])])
    def kwh(self):
        return int(self.mould.work_center) * 0.0536842105263158
    
    kes_kw = models.DecimalField(blank=True, max_digits=10, decimal_places=2)

    @computed(models.DecimalField(blank=True, max_digits=10, decimal_places=2), depends=[('mould', ['work_center'])])
    def kes_hr(self):
        return int(self.mould.work_center) * 0.0536842105263158 * float(self.kes_kw)
    
    @computed(models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2), depends=[('mould', ['cycle_time'])])
    def ct(self):
        return self.mould.cycle_time

    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['cavity_number'])])
    def cavity(self):
        return self.mould.cavity_number
    
    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['cavity_number', 'cycle_time'])])
    def u_h(self):
        return (60 * 60 * self.mould.cavity_number) / self.mould.cycle_time
    
    @computed(models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=6))
    def kes_u(self):
        return self.kes_hr / self.u_h
    
    @computed(models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=6))
    def kes_sfg(self):
        return float( self.component * self.kes_u )
    
class Labour(ComputedFieldsModel):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    component = models.IntegerField(null=True, blank=True)
    mould = models.ForeignKey(Mould, models.DO_NOTHING, blank=True, null=True)
    mac_fte = models.IntegerField(null=True, blank=True)
    cost_per_unit = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    # rate = models.ForeignKey(ExchangeRate, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fg_name} {self.sfg_name}"
    
    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['work_center'])])
    def mmts(self):
        return self.mould.work_center
    
class CompositionName(models.Model):
    composition_name = models.CharField(max_length=50, blank=True)
        
class Composition(ComputedFieldsModel):
    composition = models.ForeignKey(CompositionName, models.DO_NOTHING, blank=True, null=True)
    material_name = models.ForeignKey(RawMaterialLineItem, models.DO_NOTHING, blank=True, null=True)
    ratio = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

    @computed(models.DecimalField(blank=True, max_digits=5, decimal_places=2), depends=[('material_name', ['cost_per_kg'])])
    def price_per_kg(self):
        return self.material_name.cost_per_kg
    
    @computed(models.DecimalField(blank=True, max_digits=10, decimal_places=2))
    def price_for_ratio(self):
        return self.ratio * self.price_per_kg / 100
    
    def __str__(self):
        return f"Composition --> {self.composition.composition_name} for --> {self.material_name.material_name}"

class ChangeOver(ComputedFieldsModel):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    sfg_name = models.ForeignKey(SemiFinishedGood, models.DO_NOTHING, blank=True, null=True)
    component = models.IntegerField(null=True, blank=True)
    mould = models.ForeignKey(Mould, models.DO_NOTHING, blank=True, null=True)
    target = models.IntegerField(null=True, blank=True, default=1)
    
    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['work_center'])])
    def mmts(self):
        return self.mould.work_center
    
    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['cycle_time'])])
    def ct(self):
        return self.mould.cycle_time

    @computed(models.IntegerField(null=True, blank=True), depends=[('mould', ['cavity_number'])])
    def cavity(self):
        return self.mould.cavity_number 

    @computed(models.DecimalField(blank=True, max_digits=10, decimal_places=2))
    def max_u_m(self):
        return (60 * 60 * 24 * 30.5 * ( self.mould.cavity_number / self.mould.cycle_time))
    
    @computed(models.IntegerField(null=True, blank=True))
    def oc_hr(self):
        try:
            result = round( (15000 / 950) * int(self.mould.work_center) )
            print(result)
        except:
            result = int( (15000 / 950) )
            print(self.mould.work_center)
        return result
    
    @computed(models.DecimalField(max_digits=15, blank=True, decimal_places=2), depends=[('self', ['max_u_m', 'target'])])
    def changes(self):
        try:
            return self.max_u_m / self.target
        except:
            return 0

    @computed(models.DecimalField(blank=True, max_digits=10, decimal_places=5))
    def hrs(self):
        result = self.mould.co_time.hrs
        return result

    @computed(models.IntegerField(null=True, blank=True), depends=[('self', ['oc_hr', 'hrs', 'changes', 'target'])])
    def kes_u(self):
        try:
            return ( self.oc_hr * self.hrs * self.changes ) / self.target
        except:
            return 0
        
    def __str__(self):
        if isinstance(self.fg_name, FinishedGood) == True:
            print(type(self.fg_name))
            return f"Change over for {self.fg_name} Finished Goods"
        else:
            print(type(self.fg_name))
            return f"Change over for {self.sfg_name} Semi Finished Goods"
        
class Print(ComputedFieldsModel):
    fg_name = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=True, null=True)
    embossing = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    printing = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    labeling = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    foil = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    glue = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    shrink_wrap = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    woven_polybag = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    inner_bag = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    carton = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    strapping = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    
    @computed(models.DecimalField(blank=True, max_digits=5, decimal_places=2))
    def kes_u(self):
        return sum(self.embossing, self.printing, self.labeling, self.foil, self.glue, self.shrink_wrap, self.woven_polybag, self.inner_bag, self.carton, self.strapping)

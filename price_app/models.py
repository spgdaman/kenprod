from django.db import models
from django.conf import settings
from cogs.models import FinishedGood

class Products(models.Model):
    description = models.CharField(max_length=100)
    # description = models.ForeignKey(FinishedGood, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.description)

class MarketPrice(models.Model):
    # sales_person = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    sales_person = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_branch= models.CharField(max_length=100)
    kenpoly_product_name = models.CharField(max_length=100)
    kenpoly_price = models.IntegerField(blank=False, null=True)
    competitor_name = models.CharField(max_length=100)
    competitor_product_name = models.CharField(max_length=100)
    competitor_price = models.IntegerField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    competitor_product_image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"Entry #{self.id} on {self.created_at} by {self.sales_person}"
    

    
class Customers(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CustomerBranches(models.Model):
    name = models.CharField(max_length=100)
    parent_company = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.parent_company.name}"
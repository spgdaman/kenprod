from django.db import models
from django.conf import settings

class MarketPrice(models.Model):
    sales_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_branch= models.CharField(max_length=100)
    kenpoly_product_name = models.CharField(max_length=100)
    kenpoly_price = models.IntegerField(blank=False, null=True)
    competitor_name = models.CharField(max_length=100)
    competitor_product_name = models.CharField(max_length=100)
    competitor_price = models.IntegerField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
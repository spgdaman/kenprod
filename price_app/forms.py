from django import forms

class MarketPriceForm(forms.Form):
    customer_name = forms.CharField(label="Customer Name", required=True)
    customer_branch = forms.CharField(label="Customer Branch", required=True)
    kenpoly_product_name = forms.CharField(label="Kenpoly Product Name", required=True)
    kenpoly_price = forms.CharField(label="Kenpoly Price", required=True)
    competitor_name = forms.CharField(label="Competitor's Name", required=True)
    competitor_product_name = forms.CharField(label="Competitor's Product", required=True)
    competitor_product_image = forms.FileField(label="Competitor Product Image", required=False)
    competitor_price = forms.CharField(label="Competitor Price", required=True)
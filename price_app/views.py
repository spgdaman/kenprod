from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MarketPriceForm
from accounts.models import User
from .models import MarketPrice

def get_market_price(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MarketPriceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # data = form.save(commit=False)
            # data.user = request.user
            # data.save()

            # sales_person = User.objects.get()

            customer_name = request.POST['customer_name']
            customer_branch = request.POST['customer_branch']
            kenpoly_product_name = request.POST['kenpoly_product_name']
            kenpoly_price = request.POST['kenpoly_price']
            competitor_name = request.POST['competitor_name']
            competitor_product_name = request.POST['competitor_product_name']
            competitor_price = request.POST['competitor_price']

            market_data = MarketPrice.objects.create(
                sales_person = request.user,
                customer_name = customer_name,
                customer_branch = customer_branch,
                kenpoly_product_name = kenpoly_product_name,
                kenpoly_price = kenpoly_price,
                competitor_name = competitor_name,
                competitor_product_name = competitor_product_name,
                competitor_price = competitor_price
            )

            messages.success(request,'Data has been submitted')
            return render(request, "marketprice/price_capture.html")
    
    else:
        form = MarketPriceForm()
    
    return render(request, "marketprice/price_capture.html", {"form":form})

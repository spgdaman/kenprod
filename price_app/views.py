from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import MarketPriceForm
from accounts.models import User

def get_market_price(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MarketPriceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            return redirect("index.html")
    
    else:
        form = MarketPriceForm()
    
    return render(request, "index.html", {"form":form})

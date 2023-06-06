from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

import pandas as pd

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
            info = dict(request.POST)
            if len(info["competitor_name"]) >= 2:
                counter = len(info["competitor_name"])


                customer_name = info["customer_name"][0]
                customer_branch = info["customer_branch"][0]
                kenpoly_product_name = info["kenpoly_product_name"][0]
                kenpoly_price = info["kenpoly_price"][0]
                
                competitor_name = info["competitor_name"]
                competitor_product_name = info["competitor_product_name"]
                competitor_price = info["competitor_price"]

                market_agg = list()

                # for i in competitor_name:
                #     for j in competitor_product_name:
                #         for k in competitor_price:
                #             temp_list = [customer_name, customer_branch, kenpoly_product_name, kenpoly_price, i, j, k]
                #             print(temp_list)
                            # market_agg.append(temp_list)

                count = 0
                for item in competitor_name:
                    temp_list = [customer_name, customer_branch, kenpoly_product_name, kenpoly_price, competitor_name[count], competitor_product_name[count], competitor_price[count]]
                    market_agg.append(temp_list)
                    count = count + 1

                # print(market_agg)

                for i in market_agg:
                    market_data = MarketPrice.objects.create(
                    sales_person = request.user,
                    customer_name = i[0],
                    customer_branch = i[1],
                    kenpoly_product_name = i[2],
                    kenpoly_price = i[3],
                    competitor_name = i[4],
                    competitor_product_name = i[5],
                    competitor_price = i[6]
                )
                            

                # print(info["competitor_name"])
                # print(counter)
                # print("More than one competitor")
            
                print(market_agg)
            
            else:
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
                print(request.POST['customer_branch'])
                messages.success(request,'Data has been submitted')
                return render(request, "marketprice/price_capture.html")
    
    else:
        form = MarketPriceForm()
    
    return render(request, "marketprice/price_capture.html", {"form":form})

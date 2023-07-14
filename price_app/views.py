from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required

import pandas as pd
import io,csv

from .forms import MarketPriceForm
from accounts.models import User
from .models import MarketPrice, Products, Customers, CustomerBranches
from .filters import MarketPriceFilter
from cogs.check_groups_decorator import validate_user_in_group

class CustomerUploadView(View):
    @login_required()
    @validate_user_in_group("Sales", "Admin")
    def get(self, request):
        template_name = 'bulkupload/import.html'
        return render(request, template_name)
    
    @login_required()
    @validate_user_in_group("Sales", "Admin")
    def post(self, request):
        # print(request.FILES['data'].file)
        paramFile = io.TextIOWrapper(request.FILES['data'].file)
        portfolio = csv.DictReader(paramFile)
        list_of_dict = list(portfolio)
        objs = [row["name"] for row in list_of_dict]
        for i in objs:
            Customers.objects.create(name=i)
        
        return JsonResponse({"status_code":200})

class CustomerBranchesUploadView(View):
    @login_required()
    @validate_user_in_group("Sales", "Admin")
    def get(self, request):
        template_name = 'bulkupload/import.html'
        return render(request, template_name)
    
    @login_required()
    @validate_user_in_group("Sales", "Admin")
    def post(self, request):
        # print(request.FILES['data'].file)
        paramFile = io.TextIOWrapper(request.FILES['data'].file)
        portfolio = csv.DictReader(paramFile)
        list_of_dict = list(portfolio)
        # objs = [row["name"] for row in list_of_dict]
        for i in list_of_dict:
            id = i["id"]
            name = i["Customer Name"]
            CustomerBranches.objects.create(name=name, parent_company_id=id)
        # for i in objs:
        #     Customers.objects.create(name=i)
        
        return JsonResponse({"status_code":200})

class ProductsUploadView(View):
    @login_required()
    @validate_user_in_group("Sales", "Admin")
    def get(self, request):
        template_name = 'bulkupload/import.html'
        return render(request, template_name)
    
    @login_required()
    @validate_user_in_group("Sales", "Admin")
    def post(self, request):
        # paramFile = io.TextIOWrapper(request.FILES['productsfile'].file)
        paramFile = io.TextIOWrapper(request.FILES['data'].file)
        portfolio = csv.DictReader(paramFile)
        list_of_dict = list(portfolio)
        objs = [row['ï»¿description'] for row in list_of_dict]
        for i in objs:
            print(i)
            Products.objects.create(description=i)
        
        
        return JsonResponse({"status_code":200})
        # portfolio = csv.DictReader(paramFile)
        # list_of_dict = list(portfolio)
        # objs = [
        #     Products(
        #         description = row['description']
        #     )
        #     for row in list_of_dict
        # ]
        # try:
        #     msg = Products.objects.bul_create(objs)
        #     returnmsg = {"status_code":200}
        #     print('imported successfully')
        # except Exception as e:
        #     print('Error While Importing Data: ', e)
        #     returnmsg = {"status_code": 500}
        # return JsonResponse(returnmsg)

@login_required()
@validate_user_in_group("Sales", "Admin")
def get_market_price(request):
    products = Products.objects.all().order_by('description')
    customer_and_branches = {}
    customers = Customers.objects.all().values('pk', 'name')
    customers = [i for i in customers]
    customers = pd.DataFrame(customers)
    # customer_list = customers["name"]
    # customer_list = customer_list.to_list('records')

    branches = CustomerBranches.objects.all().values('pk', 'name', 'parent_company')
    branches = [i for i in branches]
    branches = pd.DataFrame(branches)

    try:
        total = customers.merge(branches, left_on='pk', right_on='parent_company')
        total.rename(columns = {"name_x":"customer", "name_y":"branch"}, inplace = True)
        total = total[["customer", "branch"]]
        total = (total.groupby('customer')
                .apply(lambda x: [y for y in x['branch']])
                .to_dict())
    except:
        total = branches
    
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

                user_name = f"{request.user.first_name} {request.user.last_name}"
                print(user_name)
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
                    sales_person = user_name,
                    customer_name = i[0],
                    customer_branch = i[1],
                    kenpoly_product_name = i[2],
                    kenpoly_price = i[3],
                    competitor_name = i[4],
                    competitor_product_name = i[5],
                    competitor_price = i[6]
                )
                print(f"{request.user.first_name} {request.user.first_name}")

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
                print(f"{request.user.first_name} {request.user.last_name}")
                messages.success(request,'Data has been submitted')
                return render(request, "marketprice/price_capture.html", {"form":form,"products":products,"total":total})
    
    else:
        form = MarketPriceForm()
        return render(request, "marketprice/price_capture.html", {"form":form,"products":products,"total":total})
    
    return render(request, "marketprice/price_capture.html", {"form":form,"products":products,"total":total})

@login_required()
@validate_user_in_group("Sales", "Admin")
def export_csv(request):
    # Get all market price information from the marketprice table
    marketprice = MarketPrice.objects.all()

    search = MarketPriceFilter(request.GET, queryset=marketprice).qs
    print(search)
    # Create the HttpResponse object with the appropriate CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="marketprice.csv"'

    writer = csv.writer(response)
    writer.writerow(['sales_person', 'customer_name', 'customer_branch', 'kenpoly_product_name', 'kenpoly_price', 'competitor_name', 'competitor_product_name', 'competitor_price', 'created_at'])

    for e in search.values_list('sales_person', 'customer_name', 'customer_branch', 'kenpoly_product_name', 'kenpoly_price', 'competitor_name', 'competitor_product_name', 'competitor_price', 'created_at'):
        writer.writerow(e)  
    return response
    # for price in marketprice:
    #     writer.writerow([price.sales_person, price.customer_name, price.customer_branch, price.kenpoly_product_name, price.kenpoly_price, price.competitor_name, price.competitor_product_name, price.competitor_price, price.created_at])

    # return response

@login_required()
@validate_user_in_group("Sales", "Admin")
def search(request):
    market_prices = MarketPrice.objects.all().order_by('-created_at')
    market_prices_filter = MarketPriceFilter(request.GET, queryset=market_prices)
    return render(request, 'search/market_prices_list.html', {'filter': market_prices_filter})
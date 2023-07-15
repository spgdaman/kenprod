from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExchangeRate, FinishedGood, SemiFinishedGood, RawMaterialCategory, RawMaterialLineItem, RawMaterial, ExternalComponentName, ExternalComponentLineItem, ExternalComponent, Labeling, Foiling, Packing, Power, Labour
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.views import View

from . import forms
from .check_groups_decorator import validate_user_in_group

# class LabourView(View):
#   template_name = 'cogs/labourform.html'
#   form_class = LabourForm

#   def get(self, request, *args, **kwargs):
#     form = self.form_class
#     return render(request, "cogs/labourform.html", {'form': form})

#   def post(self, request, *args, **kwargs):
#     form = self.form_class(request.POST)
#     if form.is_valid():
#       form.save()
#       return HttpResponseRedirect(reverse('list-view'))
#     else:
#       return render(request, self.template_name, {'form': form})

@login_required()
@validate_user_in_group("Finance", "Admin")
def welcome(request):
    return render(request, 'cogs/welcome.html')

@login_required()
@validate_user_in_group("Finance", "Admin")
def listings(request):
    return render(request, 'cogs/listings.html')

@login_required()
@validate_user_in_group("Finance", "Admin")
def labour_input_fg(request):
    content_type = ContentType.objects.get_for_model(Labour)
    post_permission = Permission.objects.filter(content_type=content_type)

    page_view = "Labour Cost Input Form (Finished Goods)"
    if request.method == "POST" :
        # create a form instance and populate it with data from the request:
        form = forms.LabourFormFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.LabourFormSemiFinishedGood()
            return render(request, "cogs/labourform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.LabourFormFinishedGood()
        # if request.user.has_perm("labour.Can add labour") == True:
        #     print("user can add labour cost")
        return render(request, "cogs/labourform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def labour_fg_listing(request):
    page_view = "Labour Cost Finished Goods Listing"
    labours = Labour.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/labourlisting.html", {"labours": labours, "header": page_view})


@login_required()
@validate_user_in_group("Finance", "Admin")
def labour_input_sfg(request):
    page_view = "Labour Cost Input Form (Semi-finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.LabourFormSemiFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.LabourFormSemiFinishedGood()
            return render(request, "cogs/labourform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.LabourFormSemiFinishedGood()
        return render(request, "cogs/labourform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def labour_sfg_listing(request):
    page_view = "Labour Cost Semi Finished Goods Listing"
    labours = Labour.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/labourlisting.html", {"labours": labours, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def power_input_fg(request):
    page_view = "Power Cost Input Form (Finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.PowerFormFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.PowerFormFinishedGood()
            return render(request, "cogs/powerform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.PowerFormFinishedGood()
        return render(request, "cogs/powerform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def power_fg_listing(request):
    page_view = "Power Cost Finished Goods Listing"
    powers = Power.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/powerlisting.html", {"powers": powers, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")
def power_input_sfg(request):
    page_view = "Power Cost Input Form (Semi-finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.PowerFormSemiFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')
            
            form = forms.PowerFormSemiFinishedGood()
            return render(request, "cogs/powerform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.PowerFormSemiFinishedGood()
        return render(request, "cogs/powerform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def power_sfg_listing(request):
    page_view = "Power Cost Semi Finished Goods Listing"
    powers = Power.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/powerlisting.html", {"powers": powers, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin") 
def packing_input_fg(request):
    page_view = "Packing Cost Input Form (Finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.PackingFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.PackingFormFinishedGood()
            return render(request, "cogs/packingform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.PackingFormFinishedGood()
        return render(request, "cogs/packingform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def packing_fg_listing(request):
    page_view = "Packing Cost Finished Goods Listing"
    packings = Packing.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/packinglisting.html", {"packings": packings, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")
def packing_input_sfg(request):
    page_view = "Packing Cost Input Form (Semi-finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.PackingFormSemiFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.PackingFormSemiFinishedGood()
            return render(request, "cogs/packingform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.PackingFormSemiFinishedGood()
        return render(request, "cogs/packingform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def packing_sfg_listing(request):
    page_view = "Packing Cost Semi Finished Goods Listing"
    packings = Packing.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/packinglisting.html", {"packings": packings, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def label_input_fg(request):
    page_view = "Label Cost Input Form (Finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.LabelFormFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.LabelFormFinishedGood()
            return render(request, "cogs/labelform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.LabelFormFinishedGood()
        return render(request, "cogs/labelform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def label_fg_listing(request):
    page_view = "Label Cost Finished Goods Listing"
    labels = Labeling.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/labellisting.html", {"labels": labels, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")
def label_input_sfg(request):
    page_view = "Label Cost Input Form (Semi-finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.LabelFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.LabelFormSemiFinishedGood()
            return render(request, "cogs/labelform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.LabelFormSemiFinishedGood()
        return render(request, "cogs/labelform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def label_sfg_listing(request):
    page_view = "Label Cost Semi Finished Goods Listing"
    labels = Labeling.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/labellisting.html", {"labels": labels, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")   
def foiling_input_fg(request):
    page_view = "Foiling Cost Input Form (Finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.FoilingFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.FoilingFormFinishedGood()
            return render(request, "cogs/foilingform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.FoilingFormFinishedGood()
        return render(request, "cogs/foilingform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def foiling_fg_listing(request):
    page_view = "Foiling Cost Finished Goods Listing"
    foilings = Foiling.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/foilinglisting.html", {"foilings": foilings, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")
def foiling_input_sfg(request):
    page_view = "Foiling Cost Input Form (Semi-finished Goods)"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.FoilingFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.FoilingFormSemiFinishedGood()
            return render(request, "cogs/foilingform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.FoilingFormSemiFinishedGood()
        return render(request, "cogs/foilingform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def foiling_sfg_listing(request):
    page_view = "Foiling Cost Semi Finished Goods Listing"
    foilings = Foiling.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/foilinglisting.html", {"foilings": foilings, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")   
def finished_good_input(request):
    page_view = "Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.FinishedGoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.FinishedGoodForm()
            return render(request, "cogs/finishedgoodform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.FinishedGoodForm()
        return render(request, "cogs/finishedgoodform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def fg_listing(request):
    page_view = "Finished Goods Listing"
    finishedgoods = FinishedGood.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/finishedgoodlisting.html", {"finishedgoods": finishedgoods, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def semi_finished_good_input(request):
    page_view = "Semi Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.SemiFinishedGoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.SemiFinishedGoodForm()
            return render(request, "cogs/semifinishedgoodform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.SemiFinishedGoodForm()
        return render(request, "cogs/semifinishedgoodform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def sfg_listing(request):
    page_view = "Semi Finished Goods Listing"
    semifinishedgoods = SemiFinishedGood.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/semifinishedgoodlisting.html", {"semifinishedgoods": semifinishedgoods, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")   
def raw_material_category_input(request):
    page_view = "Raw Material Name Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.RawMaterialCategoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.RawMaterialCategoryForm()
            return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.RawMaterialCategoryForm()
        return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def raw_material_line_item_input(request):
    page_view = "Raw Material Line Item Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.RawMaterialLineItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.RawMaterialLineItemForm()
            return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.RawMaterialLineItemForm()
        return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")   
def raw_material_finished_goods_input(request):
    page_view = "Raw Material Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.RawMaterialFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.RawMaterialFormFinishedGood()
            return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.RawMaterialFormFinishedGood()
        return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def rm_fg_listing(request):
    page_view = "Raw Materials Cost Finished Goods Listing"
    rawmaterials = RawMaterial.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/rawmateriallisting.html", {"rawmaterials": rawmaterials, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def raw_material_semi_finished_goods_input(request):
    page_view = "Raw Material Semi Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.RawMaterialFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.RawMaterialFormSemiFinishedGood()
            return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.RawMaterialFormSemiFinishedGood()
        return render(request, "cogs/rawmaterialform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def rm_sfg_listing(request):
    page_view = "Raw Materials Cost Semi Finished Goods Listing"
    rawmaterials = RawMaterial.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/rawmateriallisting.html", {"rawmaterials": rawmaterials, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def external_component_name_input(request):
    page_view = "External Component Name Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.ExternalComponentNameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.ExternalComponentNameForm()
            return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.ExternalComponentNameForm()
        return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def external_component_line_item_input(request):
    page_view = "External Component Line Item Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.ExternalComponentLineItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.ExternalComponentLineItemForm()
            return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.ExternalComponentLineItemForm()
        return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def external_component_finished_goods_input(request):
    page_view = "External Component Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.ExternalComponentFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.ExternalComponentFormFinishedGood()
            return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.ExternalComponentFormFinishedGood()
        return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def ec_fg_listing(request):
    page_view = "External Component Cost Finished Goods Listing"
    externalcomponents = ExternalComponent.objects.filter(fg_name__isnull=False)

    return render(request, "cogs/externalcomponentlisting.html", {"externalcomponents": externalcomponents, "header": page_view})

@login_required()
@validate_user_in_group("Finance", "Admin")    
def external_component_semi_finished_goods_input(request):
    page_view = "External Component Semi Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.ExternalComponentFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.ExternalComponentFormSemiFinishedGood()
            return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.ExternalComponentFormSemiFinishedGood()
        return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
@login_required()
@validate_user_in_group("Finance", "Admin")    
def ec_sfg_listing(request):
    page_view = "External Component Cost Semi Finished Goods Listing"
    externalcomponents = ExternalComponent.objects.filter(sfg_name__isnull=False)

    return render(request, "cogs/externalcomponentlisting.html", {"externalcomponents": externalcomponents, "header": page_view})
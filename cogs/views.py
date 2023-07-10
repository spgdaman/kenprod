from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExchangeRate, FinishedGood, SemiFinishedGood, RawMaterialCategory, RawMaterialLineItem, RawMaterial, ExternalComponentName, ExternalComponentLineItem, ExternalComponent, Labeling, Foiling, Packing, Power, Labour
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

from django.contrib import messages
from django.views import View

from . import forms

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

def labour_input_fg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.LabourFormFinishedGood(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,'Data has been submitted')

            form = forms.LabourFormSemiFinishedGood()
            return render(request, "cogs/labourform.html", {"form":form})
    
    else:
        form = forms.LabourFormFinishedGood()
        return render(request, "cogs/labourform.html", {"form":form})

def labour_input_sfg(request):
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
            return render(request, "cogs/labourform.html", {"form":form})
    
    else:
        form = forms.LabourFormSemiFinishedGood()
        return render(request, "cogs/labourform.html", {"form":form})
    
def power_input_fg(request):
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
            return render(request, "cogs/powerform.html", {"form":form})
    
    else:
        form = forms.PowerFormFinishedGood()
        return render(request, "cogs/powerform.html", {"form":form})

def power_input_sfg(request):
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
            return render(request, "cogs/powerform.html", {"form":form})
    
    else:
        form = forms.PowerFormSemiFinishedGood()
        return render(request, "cogs/powerform.html", {"form":form})
    
def packing_input_fg(request):
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
            return render(request, "cogs/packingform.html", {"form":form})
    
    else:
        form = forms.PackingFormFinishedGood()
        return render(request, "cogs/packingform.html", {"form":form})

def packing_input_sfg(request):
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
            return render(request, "cogs/packingform.html", {"form":form})
    
    else:
        form = forms.PackingFormSemiFinishedGood()
        return render(request, "cogs/packingform.html", {"form":form})
    
def label_input_fg(request):
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
            return render(request, "cogs/labelform.html", {"form":form})
    
    else:
        form = forms.LabelFormFinishedGood()
        return render(request, "cogs/labelform.html", {"form":form})

def label_input_sfg(request):
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
            return render(request, "cogs/labelform.html", {"form":form})
    
    else:
        form = forms.LabelFormSemiFinishedGood()
        return render(request, "cogs/labelform.html", {"form":form})
    
def foiling_input_fg(request):
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
            return render(request, "cogs/foilingform.html", {"form":form})
    
    else:
        form = forms.FoilingFormFinishedGood()
        return render(request, "cogs/foilingform.html", {"form":form})

def foiling_input_sfg(request):
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
            return render(request, "cogs/foilingform.html", {"form":form})
    
    else:
        form = forms.FoilingFormSemiFinishedGood()
        return render(request, "cogs/foilingform.html", {"form":form})
    
def finished_good_input(request):
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
            return render(request, "cogs/finishedgoodform.html", {"form":form})
    
    else:
        form = forms.FinishedGoodForm()
        return render(request, "cogs/finishedgoodform.html", {"form":form})
    
def semi_finished_good_input(request):
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
            return render(request, "cogs/semifinishedgoodform.html", {"form":form})
    
    else:
        form = forms.SemiFinishedGoodForm()
        return render(request, "cogs/semifinishedgoodform.html", {"form":form})
    
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
    
def external_component_semi_finished_goods_input(request):
    page_view = "External Component Semi Finished Goods Input Form"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.ExternalComponentFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
    
    else:
        form = forms.ExternalComponentFormSemiFinishedGood()
        return render(request, "cogs/externalcomponentform.html", {"form":form, "header":page_view})
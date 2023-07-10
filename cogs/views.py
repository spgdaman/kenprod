from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExchangeRate, FinishedGood, SemiFinishedGood, RawMaterialCategory, RawMaterialLineItem, RawMaterial, ExternalComponentName, ExternalComponentLineItem, ExternalComponent, Labeling, Foiling, Packing, Power, Labour
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

from django.contrib import messages
from django.views import View

from .forms import LabourFormFinishedGood,LabourFormSemiFinishedGood, PackingFormFinishedGood, PackingFormSemiFinishedGood,PowerFormFinishedGood,PowerFormSemiFinishedGood, LabelFormFinishedGood,LabelFormSemiFinishedGood, FoilingFormFinishedGood, FoilingFormSemiFinishedGood, FinishedGoodForm, SemiFinishedGoodForm

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
        form = LabourFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/labourform.html", {"form":form})
    
    else:
        form = LabourFormFinishedGood()
        return render(request, "cogs/labourform.html", {"form":form})

def labour_input_sfg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LabourFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/labourform.html", {"form":form})
    
    else:
        form = LabourFormSemiFinishedGood()
        return render(request, "cogs/labourform.html", {"form":form})
    
def power_input_fg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PowerFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/powerform.html", {"form":form})
    
    else:
        form = PowerFormFinishedGood()
        return render(request, "cogs/powerform.html", {"form":form})

def power_input_sfg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PowerFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/powerform.html", {"form":form})
    
    else:
        form = PowerFormSemiFinishedGood()
        return render(request, "cogs/powerform.html", {"form":form})
    
def packing_input_fg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PackingFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/packingform.html", {"form":form})
    
    else:
        form = PackingFormFinishedGood()
        return render(request, "cogs/packingform.html", {"form":form})

def packing_input_sfg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PackingFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/packingform.html", {"form":form})
    
    else:
        form = PackingFormSemiFinishedGood()
        return render(request, "cogs/packingform.html", {"form":form})
    
def label_input_fg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LabelFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/labelform.html", {"form":form})
    
    else:
        form = LabelFormFinishedGood()
        return render(request, "cogs/labelform.html", {"form":form})

def label_input_sfg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LabelFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/labelform.html", {"form":form})
    
    else:
        form = LabelFormSemiFinishedGood()
        return render(request, "cogs/labelform.html", {"form":form})
    
def foiling_input_fg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FoilingFormFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/foilingform.html", {"form":form})
    
    else:
        form = FoilingFormFinishedGood()
        return render(request, "cogs/foilingform.html", {"form":form})

def foiling_input_sfg(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FoilingFormSemiFinishedGood(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/foilingform.html", {"form":form})
    
    else:
        form = FoilingFormSemiFinishedGood()
        return render(request, "cogs/foilingform.html", {"form":form})
    
def finished_good_input(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FinishedGoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/finishedgoodform.html", {"form":form})
    
    else:
        form = FinishedGoodForm()
        return render(request, "cogs/finishedgoodform.html", {"form":form})
    
def semi_finished_good_input(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SemiFinishedGoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.success(request,'Data has been submitted')
            return render(request, "cogs/semifinishedgoodform.html", {"form":form})
    
    else:
        form = SemiFinishedGoodForm()
        return render(request, "cogs/semifinishedgoodform.html", {"form":form})
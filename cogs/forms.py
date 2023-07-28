from django import forms
# from .models import Labeling, Labour, FinishedGood, SemiFinishedGood, Power, Packing, Foiling
from . import models

# class LabourFormFinishedGood(forms.ModelForm):
#     class Meta:
#         model = Labour
    
#     description = forms.CharField()
#     unit = forms.IntegerField()
#     cost_per_unit = forms.DecimalField()
#     finished_good = forms.ModelMultipleChoiceField(
#         queryset=FinishedGood.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )


# class LabourFormFinishedGood(forms.ModelForm):
#     # add a field to select the finished good
#     # finished_good = forms.ModelChoiceField(FinishedGood.objects.all())

#     class Meta:
#         fields = ('description', 'unit', 'cost_per_unit', 'finished_good')
#         model = Labour

#     description = forms.CharField()
#     unit = forms.IntegerField()
#     cost_per_unit = forms.DecimalField()
#     finished_good = forms.ModelMultipleChoiceField(
#         queryset=FinishedGood.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )


# class FinishedGoodSelect(forms.Select):
#     def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
#         option = super().create_option(name, value, label, selected, index, subindex, attrs)
#         if value:
#             option['attrs']['fg-name'] = value.instance.price
#         return option
    
class LabourFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Labour
        fields = ['fg_name', 'component', 'mould', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class LabourFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Labour
        fields = ['sfg_name', 'component', 'mould', 'cost_per_unit']

class PowerFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Power
        fields = ['fg_name', 'component', ]
        # widgets = {'FinishedGood': FinishedGoodSelect}

class PowerFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Power
        fields = ['sfg_name', 'component', ]

class PackingFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Packing
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class PackingFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Packing
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class LabelFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Labeling
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class LabelFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Labeling
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class FoilingFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Foiling
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class FoilingFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.Foiling     
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class FinishedGoodForm(forms.ModelForm):
    class Meta:
        model = models.FinishedGood
        fields = ['name', 'weight']

class SemiFinishedGoodForm(forms.ModelForm):
    class Meta:
        model = models.SemiFinishedGood
        fields = ['name', 'weight']

class RawMaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = models.RawMaterialCategory
        fields = ['material_name']

class RawMaterialLineItemForm(forms.ModelForm):
    class Meta:
        model = models.RawMaterialLineItem
        fields = ['material_name', 'raw_material_cost', 'landing_cost']

class RawMaterialFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.RawMaterial
        fields = ['fg_name', 'raw_material']

class RawMaterialFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.RawMaterial
        fields = ['sfg_name', 'raw_material']

class ExternalComponentNameForm(forms.ModelForm):
    class Meta:
        model = models.ExternalComponentName
        fields = ['name']

class ExternalComponentLineItemForm(forms.ModelForm):
    class Meta:
        model = models.ExternalComponentLineItem
        fields = ['name', 'unit', 'price_per_unit']

class ExternalComponentFormFinishedGood(forms.ModelForm):
    class Meta:
        model = models.ExternalComponent
        fields = ['fg_name', 'component']


class ExternalComponentFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = models.ExternalComponent
        fields = ['component']
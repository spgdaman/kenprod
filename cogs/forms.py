from django import forms
from .models import Labeling, Labour, FinishedGood, SemiFinishedGood, Power, Packing, Foiling

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
        model = Labour
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class LabourFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = Labour
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class PowerFormFinishedGood(forms.ModelForm):
    class Meta:
        model = Power
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class PowerFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = Power
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class PackingFormFinishedGood(forms.ModelForm):
    class Meta:
        model = Packing
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class PackingFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = Packing
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class LabelFormFinishedGood(forms.ModelForm):
    class Meta:
        model = Labeling
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class LabelFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = Labeling
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class FoilingFormFinishedGood(forms.ModelForm):
    class Meta:
        model = Foiling
        fields = ['description', 'fg_name', 'unit', 'cost_per_unit']
        # widgets = {'FinishedGood': FinishedGoodSelect}

class FoilingFormSemiFinishedGood(forms.ModelForm):
    class Meta:
        model = Foiling     
        fields = ['description', 'sfg_name', 'unit', 'cost_per_unit']

class FinishedGoodForm(forms.ModelForm):
    class Meta:
        model = FinishedGood
        fields = ['name', 'unit', 'cost_per_unit']

class SemiFinishedGoodForm(forms.ModelForm):
    class Meta:
        model = SemiFinishedGood
        fields = ['name', 'fg_name', 'unit', 'cost_per_unit']
from django import forms
from django.forms import NumberInput, Select

class SquareFeetForm(forms.Form):
    squarefeet = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Square Feet', min_value=1000, max_value=2999, step_size=100)

class BedroomsForm(forms.Form):
    squarefeet = forms.IntegerField(widget=forms.HiddenInput(), label='Square Feet', min_value=1000, max_value=2999, step_size=100)
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False, label='Bedrooms', min_value=2, max_value=5, step_size=1)

class BathroomsForm(forms.Form):
    squarefeet = forms.IntegerField(widget=forms.HiddenInput(), label='Square Feet', min_value=1000, max_value=2999, step_size=100)
    bedrooms = forms.IntegerField(widget=forms.HiddenInput(), label='Bedrooms', min_value=2, max_value=5, step_size=1)
    bathrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False, label='Bathrooms', min_value=1, max_value=3, step_size=1)

class NeighborhoodForm(forms.Form):
    squarefeet = forms.IntegerField(widget=forms.HiddenInput(), label='Square Feet', min_value=1000, max_value=2999, step_size=100)
    bedrooms = forms.IntegerField(widget=forms.HiddenInput(), label='Bedrooms', min_value=2, max_value=5, step_size=1)
    bathrooms = forms.IntegerField(widget=forms.HiddenInput(), label='Bathrooms', min_value=1, max_value=3, step_size=1)
    neighborhood = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=False, label='Neighborhood', choices=[(0, "Rural"), (1, "Suburb"), (2, "Urban")])

class ModelForm(forms.Form):
    squarefeet = forms.IntegerField(widget=forms.HiddenInput(), label='Square Feet', min_value=1000, max_value=2999, step_size=100)
    bedrooms = forms.IntegerField(widget=forms.HiddenInput(), label='Bedrooms', min_value=2, max_value=5, step_size=1)
    bathrooms = forms.IntegerField(widget=forms.HiddenInput(), label='Bathrooms', min_value=1, max_value=3, step_size=1)
    neighborhood = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), label='Neighborhood', choices=[(0, "Rural"), (1, "Suburb"), (2, "Urban")])

   
from dal import autocomplete
from django import forms
from models import *
from school.models import School

class CityChoiceForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_town']
        widgets = {
            'school_town': autocomplete.ModelSelect2(url='city-autocomplete')
        }
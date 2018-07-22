from django import forms
from models import *



class ReviewInstructorAddForm(forms.ModelForm):
    class Meta:
        model = ReviewInstructor
        fields = '__all__'
        exclude = ['instructor','born']

class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedbackinstructor
        fields= '__all__'

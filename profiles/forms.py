# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from .models import *
from school.models import *
from instructors.models import *
from captcha.fields import CaptchaField
from dal import autocomplete

class EditSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('__all__')
        widgets = {
            'school_town': autocomplete.ModelSelect2(url='city-autocomplete')
        }
        
class SignupForm(forms.ModelForm):
    CHOICES = (
        ('1','Инструктор'),
        ('2', 'Автошкола'),
        )
    profile_status = forms.ChoiceField(choices=CHOICES, label=u"Кто вы", widget=forms.RadioSelect())
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.profile.status = self.cleaned_data['profile_status']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__' 
        
class SchoolAddForm(forms.ModelForm):
    captcha = CaptchaField()
    category_education = forms.ModelMultipleChoiceField(queryset=Category_education.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label=u"Категории")
    class Meta:
        model = School
        fields = '__all__'
        exclude = ['user','slug','premium', 'text_unique_price', 'date_off_premium','city']

class SchoolSocialForm(forms.ModelForm):
    captcha = CaptchaField()
    category_education = forms.ModelMultipleChoiceField(queryset=Category_education.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label=u"Категории")
    class Meta:
        model = School
        fields = ['vk','od','fc','tw']

class BranchEditForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        exclude = ['school']

class AutodromeAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Autodrome
        fields = '__all__'
        exclude = ['school']

class SchoolImageAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = SchoolImage
        fields = '__all__'
        exclude = ['school']
        
        
class SchoolDocumentAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = SchoolDocument
        fields = '__all__'
        exclude = ['school']    


class InstructorAddForm(forms.ModelForm):
    captcha = CaptchaField()
    category_education = forms.ModelMultipleChoiceField(queryset=Category_education.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label=u"Категории")
    car_akpp = forms.CharField(label=u'Первый автомобиль', widget=forms.TextInput(attrs={'placeholder': 'Лада Гранта АКПП'}))
    car_mkpp = forms.CharField(label=u'Второй автомобиль', widget=forms.TextInput(attrs={'placeholder': 'Лада Гранта МКПП'}))
    class Meta:
        model = Instructor
        fields = '__all__'
        exclude = ['user','premium','slug']

class BillAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Bill
        fields = '__all__'
        exclude = ['user']
from django import forms
from captcha.fields import CaptchaField
from models import *

class NewsAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = News
        fields = '__all__'
        exclude = ('slug','user','publish')
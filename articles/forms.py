from django import forms
from models import *
from captcha.fields import CaptchaField

class ArticleAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('slug','user','publish')

class FaqForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Faq
        fields = '__all__'
        exclude = ('answer','born','public')
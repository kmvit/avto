from dal import autocomplete
from easy_maps.widgets import AddressWithMapWidget
from django import forms
from models import *
from captcha.fields import CaptchaField

class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('__all__')
  

class AddSchoolForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = School
        fields = '__all__'
        exclude = ['text_unique_price', 'date_off_premium']

class ReviewAddForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['school','born']
        
    def form_valid(self,form):
        self.object = form.save(commit=False)
        school = get_object_or_404(School, slug=self.kwargs['slug'])
        self.object.school = school
        self.object.save()
        subject = 'Confirm'
        message = 'id'
        from_email = 'justscoundrel@yandex.ru'
        send_mail(subject, message, from_email, ['asdasd@ya.ru'])
        return super(ReviewAdd, self).form_valid(form)
        
        
class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedbackschool
        fields= '__all__'
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(), max_length=1000)
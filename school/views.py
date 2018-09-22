# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, HttpResponse, get_object_or_404
from models import *
from forms import *
from news.models import *
from articles.models import *
from instructors.models import Instructor
from dal import autocomplete
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Sum
from geopy.geocoders import Nominatim
from django.db.models import Count, Avg, Max, Min
import urllib
import codecs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.core.mail import EmailMessage, send_mail, mail_admins
import json
from django.http import HttpResponseBadRequest
import re
from urllib2 import urlopen
from urllib import quote
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import geocoder
from avto.settings_local import ID_SENDER_SMS_RU
# Create your views here.


def add_city(request):
    school_list = School.objects.all()
    for item in school_list:
        item.city = item.school_town.title
        item.save()

        

class Home(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        if 'pst' in self.request.COOKIES:
            city = Town.objects.get(id = self.request.COOKIES['pst'])

            context['city'] = city
            schools = School.objects.filter(school_town=city).annotate(avg_review=Avg('review__rating')).order_by('-premium','-avg_review')
        else:
            schools = School.objects.annotate(avg_review=Avg('review__rating')).order_by('-premium','-avg_review')
        school_list = [] # Сделано для правильного вывода школ по рейтингу с использование пагинации
        for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
            if item.avg_review != None or item.premium:
                school_list.append(item)
        for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
            if item.avg_review == None and item.premium == False:
                school_list.append(item)
        paginator = Paginator(school_list, 10) # Show 10 contacts per page
        page = self.request.GET.get('page')
        try:
            school_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            school_list = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            school_list = paginator.page(paginator.num_pages)
        context['school_list'] = school_list
        context['article_list'] = Article.objects.filter(publish=True)
        context['news'] = News.objects.filter(publish=True)
        return context
        

class SchoolList(ListView):
    model = School
    def get_context_data(self, **kwargs):
        context = super(SchoolList, self).get_context_data(**kwargs)
        if 'pst' in self.request.COOKIES:
            city = Town.objects.get(id = self.request.COOKIES['pst'])
            
            
            
            schools = School.objects.filter(school_town=city).annotate(avg_review=Avg(models.Case(models.When(review__verificated=True, then='review__rating'), output_field=models.IntegerField()))).order_by('-premium','-avg_review')
            
            school_list = [] # Сделано для правильного вывода школ по рейтингу с использование пагинации
            for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review != None or item.premium:
                    school_list.append(item)
            for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review == None and item.premium == False:
                    school_list.append(item)
            paginator = Paginator(school_list, 10) # Show 10 contacts per page
            page = self.request.GET.get('page')
            try:
                school_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                school_list = paginator.page(1)
            except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
                school_list = paginator.page(paginator.num_pages)
            context['school_list'] = school_list
            context['city']=city
        else:
            schools = School.objects.annotate(avg_review=Avg('review__rating')).order_by('-premium','-avg_review')
            school_list = [] # Сделано для правильного вывода школ по рейтингу с использование пагинации
            for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review != None or item.premium:
                    school_list.append(item)
            for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review == None and item.premium == False:
                    school_list.append(item)
            paginator = Paginator(school_list, 10) # Show 10 contacts per page
            page = self.request.GET.get('page')
            try:
                school_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                school_list = paginator.page(1)
            except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
                school_list = paginator.page(paginator.num_pages)
            context['school_list'] = school_list
        context['review_sum'] = Review.objects.annotate(avg_rating=Avg('rating'))
        
        return context
        
        

        
class SchoolDetail(DetailView):
    model = School
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SchoolDetail, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(premium = True, school_town = self.object.school_town).order_by('?')
        context['review_list'] = Review.objects.filter(school__slug=self.kwargs['slug'], verificated = True).order_by('-born')
        context['review_sum'] = School.objects.filter(slug=self.kwargs['slug']).annotate(avg_review=Avg(models.Case(models.When(review__verificated=True, then='review__rating'), output_field=models.IntegerField())))
        context['review_count'] = Review.objects.filter(school__slug=self.kwargs['slug'], verificated = True).count()
        context['school_list_side'] = School.objects.filter(school_town= self.object.school_town).annotate(avg_review=Avg('review__rating')).order_by('-premium','-avg_review')
        context['instructor_list'] =instructors = Instructor.objects.filter(city=self.object.school_town).annotate(avg_review=Avg('reviewinstructor__rating')).order_by('-premium','-avg_review')
        return context
        
class ReviewDetail(ListView):
    model = Review
    def get_context_data(self, **kwargs):
        context = super(ReviewsDetail, self).get_context_data(**kwargs)
        return context
        
class ReviewsList(ListView):
    model = Review
    def get_queryset(self):
        return Review.objects.filter(school__slug=self.kwargs['slug'], verificated = True).order_by('-born')
    
    def get_context_data(self, **kwargs):
        context = super(ReviewsList, self).get_context_data(**kwargs)
        context['school'] = School.objects.get(slug=self.kwargs['slug'])
        return context

class ReviewAdd(CreateView):
    model = Review
    form_class = ReviewAddForm
    template_name = 'school/review_add.html'
    success_url = 'reviewsend'
    
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        school = get_object_or_404(School, slug=self.kwargs['slug'])
        self.object.school = school
        
        self.object.save()
        LogEntry.objects.log_action(
            user_id=school.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=str(self.object),
            action_flag=ADDITION)
        slug = self.kwargs['slug']
        subject = 'Отзыв'
        message = u'Перейдите по ссылке для активации отзыва ' + 'http://vodibezopasno.com/school/' + '%s' % slug + '/verification/' + '%s' % self.object.id
        email = form.cleaned_data['email']
        from_email = 'info@vodibezopasno.com'
        send_mail(subject, message, from_email, [email,])
        d=Context({
            'name':self.object.name,
            'user':self.object.school.user,
            'school':self.object.school,
        })
        htmly = get_template('email/myfile.html')
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [self.object.school.email,])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super(ReviewAdd, self).form_valid(form)

def ReviewVerificathion(request, pk, slug):
    school = School.objects.get(slug=slug)
    review_list = Review.objects.filter(school=school)
    review = Review.objects.get(id=pk)
    for item in review_list:
        if item.email == review.email and item.verificated:
            context = {'review':review, 'school':school}
            return render(request, 'school/not_success_review_add.html', context)
    
    review.verificated = True
    review.save()
    context = {'review':review, 'school':school }
    return render(request, 'school/success_review_add.html', context)
        
def ReviewSend(request,slug):
    return render(request, 'school/review_send.html')
    
class ReviewResponceAdd(CreateView):
    """
     Добавить ответ на отзыв
    """
    model = ReviewResponce
    form_class = ReviewAddForm
    template_name = 'school/review_add.html'
    success_url = 'reviewsend'
    
    def form_valid(self,form):
        subject = 'Отзыв'
        from_email = 'info@vodibezopasno.com'
        d=Context({
            'name':obj.reviewname,
            'school':obj.review.school,
        })
        htmly = get_template('email/response_review.html')
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [self.object.email,])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super(ReviewResponceAdd, self).form_valid(form)

class BranchList(ListView):
    """Адреса филиалов школы"""
    model = Branch
    def get_queryset(self):
        return Branch.objects.filter(school__slug=self.kwargs['slug'])
        
    def get_context_data(self, **kwargs):
        context = super(BranchList, self).get_context_data(**kwargs)
        school = School.objects.get(slug=self.kwargs['slug'])
        g = geocoder.google(school.adress, local='ru')
        context['coordinate'] = g.latlng
        context['school'] = school
        context['autodrome_list'] = Autodrome.objects.filter(school__slug=self.kwargs['slug'])
        return context

class SchoolImageList(ListView):
    model = SchoolImage
    def get_queryset(self):
        return SchoolImage.objects.filter(school__slug=self.kwargs['slug'])
        
    def get_context_data(self, **kwargs):
        context = super(SchoolImageList, self).get_context_data(**kwargs)
        context['school'] = School.objects.get(slug=self.kwargs['slug'])
        return context
        
class SchoolDocumentList(ListView):
    """
    Отображение документов школы на детальной странице
    """
    model = SchoolDocument
    def get_queryset(self):
        return SchoolDocument.objects.filter(school__slug=self.kwargs['slug'])
        
    def get_context_data(self, **kwargs):
        context = super(SchoolDocumentList, self).get_context_data(**kwargs)
        context['school'] = School.objects.get(slug=self.kwargs['slug'])
        return context
        
        
        
class CitySearchList(ListView):
    model = School
    def get_context_data(self,**kwargs):
        context = super(CitySearchList, self).get_context_data(**kwargs)
        context['review_sum'] = Review.objects.annotate(avg_rating=Avg('rating'))
        context['school_list'] = School.objects.filter(city=self.request.GET['s']).annotate(avg_review=Avg('review__rating'))
        context['city_name'] = self.request.GET['s']
        return context    
    
class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs
        
class DocumentList(ListView):
    model = Document
    
    
from django.core.mail import send_mail

def sender(request):
    send_mail('Subject here', 'Here is the message.', 'justscoundrel@yandex.ru', ['justscoundrel@yandex.ru'])
    return HttpResponse('ok')


def reviewresponce(request,id):
    if request.POST:
        review = Review.objects.get(id = request.POST['review_id'])
        response = ReviewResponce.objects.create(review_id = id, body=request.POST['text'])
        response.save()
        subject = 'Отзыв'
        from_email = 'info@vodibezopasno.com'
        d=Context({
            'name':review.name,
            'school':review.school,
        })
        htmly = get_template('email/response_review.html')
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [review.email,])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        context = {'school':review.school,}
    else:
        return HttpResponse('Not good')
    return render(request, 'school/reviewresponce_success.html',context)
    
class FeedbackschoolList(ListView):
    """
    Онлайн заявки школ
    """
    model = Feedbackschool

 
    
    def get_queryset(self):
        qs = super(FeedbackschoolList, self).get_queryset()
        user = self.request.user
        school = School.objects.get(slug=self.kwargs['slug'])
        if school.user == user:
            return qs.filter(school=school)
        else:
            return qs.none()
 
    
class Feedbackschool(CreateView):
    model = Feedbackschool
    form_class = Feedbackform
    template_name = 'school/success.html'
    success_url = 'success'
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        school = School.objects.get(id=self.request.POST['school'])
        name = self.request.POST['name']
        phone = self.request.POST['phone']

        idsender = ID_SENDER_SMS_RU
        message_sms = u'Vodibezopasno.com заявка от ' + u'%s' % name + u", телефон:" + '%s' % phone
        text = message_sms.encode('utf8')
        subject = quote(text)
        s = school.phone_number
        reg = re.compile('[^0-9 ]')
        phone_school = (reg.sub('', s))
        to = phone_school
        #return HttpResponse(phone_number)
        url = "http://sms.ru/sms/send?api_id=%s&text=%s&to=%s" % (idsender, subject, to)
        res = urlopen(url)
        
        message = u'Сообщение с сайта vodibezopasno.com. Вам поступила заявка от ' + '%s' % name + u", Телефон:" + '%s' % phone
        send_mail('Заявка на обучение.', message, 'info@vodibezopasno.com', [school.email])

        return super(Feedbackschool, self).form_valid(form)
    
    def form_invalid(self,form):
        return render(self.request, 'school/notsuccess.html', {'form':form})
        
def success(request,slug):
    return render(request, 'school/success.html')


from django.contrib.syndication.views import Feed



class LatestSchoolsFeed(Feed):
    title = "Список Автошкол"
    description = "rss канал списка автошкол"
    description_template = "feeds/school_feeds.html"
    link = "/schools/"

    def items(self):
        return School.objects.all()

from django.contrib.sitemaps import Sitemap

class SchoolSitemap(Sitemap):
    protocol = 'https'
    def items(self):
        return School.objects.all()



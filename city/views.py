# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, render_to_response, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Sum
from geopy.geocoders import Nominatim
from django.db.models import Count, Avg, Max, Min
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.core.mail import EmailMessage, send_mail, mail_admins
# Create your views here.

from school.models import School, Review
from models import *
from dal import autocomplete
from instructors.models import *


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):


        qs = Town.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs
        
        

class CitySchoolList(DetailView):
    model = Town
    template_name = 'city/city_school_list.html'
    def get_object(self, **kwargs):
        return get_object_or_404(Town, slug=self.kwargs['slug'])
        
    def get_context_data(self, **kwargs):
        context = super(CitySchoolList, self).get_context_data(**kwargs)
        schools = School.objects.filter(school_town=self.object).annotate(avg_review=Avg(models.Case(models.When(review__verificated=True, then='review__rating'), output_field=models.IntegerField()))).order_by('-premium','-avg_review')
            
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
        
class CityInstructorList(DetailView):
    model = Town
    template_name = 'city/city_instructor_list.html'
    def get_context_data(self, **kwargs):
        context = super(CityInstructorList, self).get_context_data(**kwargs)
        if 'pst' in self.request.COOKIES:
            city = Town.objects.get(id = self.request.COOKIES['pst'])
            instructors = Instructor.objects.filter(instructor_town=city).annotate(avg_review=Avg(models.Case(models.When(reviewinstructor__verificated=True, then='reviewinstructor__rating'), output_field=models.IntegerField()))).order_by('-premium', '-avg_review')
            instructor_list = [] # Сделано для правильного вывода инструкторов по рейтингу с использование пагинации
            for item in instructors: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review != None or item.premium:
                    instructor_list.append(item)
            for item in instructors: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review == None and item.premium == False:
                    instructor_list.append(item)
            paginator = Paginator(instructor_list, 10) # Show 10 contacts per page
            page = self.request.GET.get('page')
            try:
                instructor_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                instructor_list = paginator.page(1)
            except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
                instructor_list = paginator.page(paginator.num_pages)
            context['instructor_list'] = instructor_list
            context['city']=city
        else:
            context['instructor_list'] = Instructor.objects.annotate(avg_review=Avg(models.Case(models.When(reviewinstructor__verificated=True, then='reviewinstructor__rating'), output_field=models.IntegerField()))).order_by('-premium','-avg_review')
        context['review_sum'] = ReviewInstructor.objects.annotate(avg_rating=Avg('rating'))
        
        return context
        
def redirect_city(request):
    city = get_object_or_404(Town,id=request.GET['school_town'])
    return redirect('city:city_school_list', slug=city.slug, )
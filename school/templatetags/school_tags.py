# -*- coding: utf-8 -*-
from django import template
from school.models import School
from footerpage.models import *
from instructors.models import Instructor
from django.db.models import Count, Avg, Max, Min
import urllib
import codecs
from city.models import Town

register = template.Library()
@register.inclusion_tag('school/sidebar.html', takes_context=True)
def best(context):
    request = context['request']
    if 'pst' in request.COOKIES:
            city = Town.objects.get(id = request.COOKIES['pst'])
            schools = School.objects.filter(school_town=city).annotate(avg_review=Avg(models.Case(models.When(review__verificated=True, then='review__rating'), output_field=models.IntegerField()))).order_by('-premium','-avg_review')
            school_list_side = [] # Сделано для правильного вывода школ по рейтингу с использование пагинации
            for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review != None or item.premium:
                    school_list_side.append(item)
            for item in schools: # Два цикла для того чтобы поставить школы без рейтинга в конец цикла.
                if item.avg_review == None and item.premium == False:
                    school_list_side.append(item)
            instructor_list = Instructor.objects.filter(city=city).annotate(avg_review=Avg(models.Case(models.When(reviewinstructor__verificated=True, then='reviewinstructor__rating'), output_field=models.IntegerField()))).order_by('-premium','-avg_review')
    else:
            school_list_side = School.objects.annotate(avg_review=Avg('review__rating')).order_by('-premium','-avg_review')
            instructor_list = Instructor.objects.annotate(avg_review=Avg('reviewinstructor__rating')).order_by('-premium','-avg_review')
    context_dict = {'school_list_side':school_list_side, 'instructor_list': instructor_list}
    return context_dict
    
    
@register.inclusion_tag('footer_menu.html', takes_context=True)
def page(context):
    request = context['request']
    page_list = Page.objects.all()
    context_dict = {'page_list':page_list}
    return context_dict
    

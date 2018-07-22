# -*- coding: utf-8 -*-
from django import template
from city.models import *
from city.forms import *
from school.models import School
from footerpage.models import *
from instructors.models import Instructor
from django.db.models import Count, Avg, Max, Min
import urllib
import codecs
from django.shortcuts import HttpResponse, get_object_or_404, redirect

register = template.Library()
@register.inclusion_tag('city/city_in_header.html', takes_context=True)
def city_title(context):
    request = context['request']
    if 'pst' in request.COOKIES:
        city = Town.objects.get(id = request.COOKIES['pst'])
        context_dict = {'city':city}
        return context_dict


@register.inclusion_tag('city/select_city.html', takes_context=True)
def accept_city(context):
    request = context['request']
    if 'pst' in request.COOKIES:
        city = Town.objects.get(id = request.COOKIES['pst'])
        for item in Town.objects.all():
            if item.title == city.title:
                context_dict = {'city':item}
              

                return context_dict
            
@register.inclusion_tag('city/city_choice.html', takes_context=True)            
def city_choice(context):
    request = context['request']
    if 'pst' in request.COOKIES:
        city = Town.objects.get(id = request.COOKIES['pst'])
        form = CityChoiceForm()
        context_dict = {'city': city, 'form': form}
    else:
        form = CityChoiceForm()
        context_dict = {'form': form }
    return context_dict

@register.inclusion_tag('city/footer_menu_city.html', takes_context=True)            
def footer_menu_city(context):
    city_list = Town.objects.filter(in_menu = True).order_by('title')   
    context_dict = {'city_list': city_list }
    return context_dict

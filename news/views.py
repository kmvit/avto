# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from django.shortcuts import reverse, HttpResponseRedirect
from unidecode import unidecode
from django.template.defaultfilters import slugify
from django.contrib import messages
# Create your views here.

class Newslist(ListView):
    model = News
    template_name = 'news/news_list.html'
    

    def get_context_data(self, **kwargs):
        context=super(Newslist,self).get_context_data(**kwargs)
        news = News.objects.filter(publish=True)
        paginator = Paginator(news, 10) # Show 10 contacts per page
        page = self.request.GET.get('page')
        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news_list = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            news_list = paginator.page(paginator.num_pages)
        context['news_list'] = news_list
        return context
        
class Newsdetail(DetailView):
    model = News
    
    def get_context_data(self, **kwargs):
        context = super(Newsdetail, self).get_context_data(**kwargs)
        context['news_list'] = News.objects.filter(publish=True).exclude(slug=self.kwargs['slug'])
        return context
        
class NewsAdd(CreateView):
    model = News
    form_class = NewsAddForm
    template_name = 'news/news_add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.slug = slugify(unidecode(self.object.title))
        self.object.save()
        messages.success(self.request, "Ваша новость отправлена на модерацию!")
        return render(self.request, 'news/news_success.html', self.get_context_data())
    
class NewsCategory(DetailView):
    model = NewsCategory
    
    def get_context_data(self, **kwargs):
        context = super(NewsCategory, self).get_context_data(**kwargs)
        news = News.objects.filter(publish=True, category__slug = self.kwargs['slug']).exclude(slug=self.kwargs['slug'])
        paginator = Paginator(news, 10) # Show 10 contacts per page
        page = self.request.GET.get('page')
        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news_list = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            news_list = paginator.page(paginator.num_pages)
        context['news_list'] = news_list
        context['another_news'] = News.objects.filter(publish=True).exclude(category__slug = self.kwargs['slug'])
        return context
        
from django.contrib.sitemaps import Sitemap

class NewsSitemap(Sitemap):
    protocol = 'https'
    def items(self):
        return News.objects.all()

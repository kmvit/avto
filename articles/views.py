# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from unidecode import unidecode
from django.template.defaultfilters import slugify
from .forms import *
from django.contrib import messages

class CategoryDetail(DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        article_list = Article.objects.filter(category__slug = self.kwargs['slug'],publish=True)
        paginator = Paginator(article_list, 10) # Show 10 contacts per page
        page = self.request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article_list = paginator.page(paginator.num_pages)
        context['article_list']=article_list
        return context
        
class Articlelist(ListView):
    model = Article
    def get_queryset(self):
        return Article.objects.filter(publish=True)
    
    def get_context_data(self, **kwargs):
        context = super(Articlelist, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        article_list = Article.objects.filter(publish=True)
        paginator = Paginator(article_list, 10) # Show 10 contacts per page
        page = self.request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article_list = paginator.page(paginator.num_pages)
        context['article_list']=article_list
        return context

    
class Articledetail(DetailView):
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(Articledetail, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.exclude(slug=self.kwargs['slug'])
        context['category_list'] = Category.objects.all()
        return context
    
    
class ArticleAdd(CreateView):
    model = Article
    form_class = ArticleAddForm
    template_name = 'articles/article_add.html'
    success_url = '/article'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.slug = slugify(unidecode(self.object.title))
        self.object.save()
        messages.success(self.request, "Ваша статья отправлена на модерацию!")
        return render(self.request, 'news/news_success.html', self.get_context_data())

        
class FaqAdd(CreateView):
    model = Faq
    form_class = FaqForm
    success_url = '/article'
    



class FaqList(ListView):
    model = Faq
    
    def get_queryset(self):
        return Faq.objects.filter(public=True)

class FaqDetail(DetailView):
    model = Faq
    
    
from django.contrib.sitemaps import Sitemap

class ArticleSitemap(Sitemap):
    protocol = 'https'
    def items(self):
        return Article.objects.all()
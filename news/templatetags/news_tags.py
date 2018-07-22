from django import template
from news.models import *

register = template.Library()
@register.inclusion_tag('news_tag.html', takes_context=True)
def news_sidebar(context):
    request = context['request']
    news_list = News.objects.filter(publish=True) 
    context_dict = {'news':news_list,}
    return context_dict

    
@register.inclusion_tag('news_footer_tag.html', takes_context=True)
def news_footer(context):
    request = context['request']
    news_list = News.objects.filter(publish=True) 
    context_dict = {'news':news_list,}
    return context_dict
    
@register.inclusion_tag('news_category_tag.html', takes_context=True)
def news_category(context):
    request = context['request']
    category_list = NewsCategory.objects.all() 
    context_dict = {'category_list':category_list,}
    return context_dict
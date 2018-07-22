from django import template
from articles.models import *

register = template.Library()
@register.inclusion_tag('article_tags.html', takes_context=True)
def article_sidebar(context):
    request = context['request']
    article_list = Article.objects.filter(publish=True) 
    context_dict = {'article_list':article_list,}
    return context_dict

    

from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def footerpage(request,slug):
    page = get_object_or_404(Page, slug = slug)
    context = {'page':page}
    return render (request, 'footerpage-detail.html', context)
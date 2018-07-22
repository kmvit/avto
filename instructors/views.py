# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import *
from forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Sum, Count, Avg
import urllib
import codecs
from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
import re
from urllib2 import urlopen
from urllib import quote
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from avto.settings_local import ID_SENDER_SMS_RU
# Create your views here.

class InstructorList(ListView):
    model = Instructor

    def get_context_data(self, **kwargs):
        context = super(InstructorList, self).get_context_data(**kwargs)
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
        

class InstructorDetail(DetailView):
    model = Instructor
    def get_queryset(self):
        return Instructor.objects.filter(slug=self.kwargs['slug']).annotate(avg_review=Avg('reviewinstructor__rating'))
    
    def get_context_data(self, **kwargs):
        context = super(InstructorDetail, self).get_context_data(**kwargs)
        context['review_list'] = ReviewInstructor.objects.filter(instructor__slug=self.kwargs['slug'],verificated = True)
        context['review_count'] = ReviewInstructor.objects.filter(instructor__slug=self.kwargs['slug'],verificated = True).count()
        context['instructor_list'] = Instructor.objects.filter(instructor_town = self.object.instructor_town, premium = True).order_by('?')
        context['instructor_list_side_premium'] = Instructor.objects.filter(instructor_town=self.object.instructor_town, premium=True).annotate(avg_review=Avg('reviewinstructor__rating')).order_by('-premium','-avg_review')
        context['instructor_list_side'] = Instructor.objects.filter(instructor_town=self.object.instructor_town, premium=False).annotate(avg_review=Avg('reviewinstructor__rating')).order_by('-avg_review')
        return context


class ReviewInstructorAdd(CreateView):
    model = ReviewInstructor
    form_class = ReviewInstructorAddForm
    template_name = 'instructors/review_add.html'
    success_url = 'reviewsend'
    def form_valid(self,form):
        obj = form.save(commit=False)
        instructor = get_object_or_404(Instructor, slug=self.kwargs['slug'])
        obj.instructor = instructor
        obj.save()
        LogEntry.objects.log_action(
            user_id=instructor.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=obj.instructor.id,
            object_repr=str(obj),
            action_flag=ADDITION)
        slug = self.kwargs['slug']
        subject = 'Confirm'
        message = u'Перейдите по ссылке для активации отзыва ' + 'http://vodibezopasno.com/instructor/' + '%s' % slug + '/verification/' + '%s' % obj.id
        email = form.cleaned_data['email']
        from_email = 'info@vodibezopasno.com'
        send_mail(subject, message, from_email, [email,])
        
        d=Context({
            'name':obj.name,
            'user':obj.instructor.user,
            'instructor':obj.instructor.fio,
        })
        htmly = get_template('instructor_email/myfile.html')
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [obj.instructor.email,])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        return super(ReviewInstructorAdd, self).form_valid(form)
        
def ReviewVerificathion(request, pk, slug):
    instructor = Instructor.objects.get(slug=slug)
    review_list = ReviewInstructor.objects.filter(instructor=instructor).exclude(id=pk)
    review = ReviewInstructor.objects.get(id=pk)
    email_count=0
    for item in review_list:
        if item.email==review.email:
            email_count+=1
        else:
            email_count=0
    if email_count > 0:
        context = {'review':review, 'instructor':instructor}
        return render(request, 'instructors/not_success_review_add.html', context)
    else:
        review.verificated = True
        review.save()
        context = {'review':review, 'instructor':instructor }
        return render(request, 'instructors/success_review_add.html', context)
        
def ReviewSend(request,slug):
    return render(request, 'school/review_send.html')
    
def reviewresponce(request,id):
    if request.POST:
        review = ReviewInstructor.objects.get(id = request.POST['review_id'])
        response = ReviewResponceInstructor.objects.create(review_id = id, body=request.POST['text'])
        response.save()
        subject = 'Отзыв'
        from_email = 'info@vodibezopasno.com'
        d=Context({
            'name':review.name,
            'school':review.instructor,
        })
        htmly = get_template('instructor_email/responce.html')
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [review.email,])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        context = {'instructor':review.instructor,}
    else:
        return HttpResponse('Not good')
    return render(request, 'instructors/reviewresponce_success.html',context)

@method_decorator(login_required, name='dispatch')
class FeedbackinstructorList(ListView):
    """
    Онлайн заявки инструктора
    """
    model = Feedbackinstructor

 

    def get_queryset(self):
        qs = super(FeedbackinstructorList, self).get_queryset()
        user = self.request.user
        instructor = Instructor.objects.get(slug=self.kwargs['slug'])
        if instructor.user == self.request.user:
            return qs.filter(instructor=instructor)
        else:
            return qs.none()
    
    
class Feedback(CreateView):
    model = Feedbackinstructor
    form_class = Feedbackform
    template_name = 'school/success.html'
    success_url = 'success'
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        instructor = Instructor.objects.get(id=self.request.POST['instructor'])
        name = self.request.POST['name']
        phone = self.request.POST['phone']

        
        idsender = ID_SENDER_SMS_RU
        message_sms = u'Vodibezopasno.com заявка от ' + u'%s' % name + u", телефон:" + '%s' % phone
        text = message_sms.encode('utf8')
        subject = quote(text)
        s = instructor.phone_number
        reg = re.compile('[^0-9 ]')
        phone_instructor = (reg.sub('', s))
        to = phone_instructor
        #return HttpResponse(phone_number)
        url = "http://sms.ru/sms/send?api_id=%s&text=%s&to=%s" % (idsender, subject, to)
        res = urlopen(url)
        
        message = u'Сообщение с сайта vodibezopasno.com. Вам поступила заявка от ' + '%s' % name + u", Телефон:" + '%s' % phone
        send_mail('Заявка на обучение.', message, 'info@vodibezopasno.com', [instructor.email])
        return super(Feedback, self).form_valid(form)
    
    def form_invalid(self,form):
        return render(self.request, 'school/notsuccess.html', {'form':form})
        
def success(request,slug):
    return render(request, 'school/success.html')
    
from django.contrib.sitemaps import Sitemap

class InstructorSitemap(Sitemap):
    protocol = 'https'
    def items(self):
        return Instructor.objects.all()

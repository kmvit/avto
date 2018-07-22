# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, reverse, redirect, get_object_or_404, Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from school.models import *
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from unidecode import unidecode
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION



@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = User
    template_name = 'profiles/profile_detail.html'
                                                      
    def get_object(self):                                                      
        event = get_object_or_404(User, id=self.kwargs['pk'])                                      
        if self.request.user != event or self.request.user.profile.status == '3':                                              
            raise Http404()
        else:
            return event
    

@login_required
def update_profile(request, pk):
    """
    Изменить профиль (ФИО, аватар)
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profiles:profile_detail', pk=1)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'profiles/profile_update.html', {
        'user_form': user_form,
    })
    
@method_decorator(login_required, name='dispatch')    
class ProfileSchools(DetailView):
    model = User
    template_name = 'profiles/profile_schools.html'
    def get_context_data(self,**kwargs):
        context = super(ProfileSchools, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(user_id = self.object.id)
        return context
    def get_object(self):                                                      
        event = get_object_or_404(User, id=self.kwargs['pk'])                                      
        if self.request.user != event:                                              
            raise Http404()
        else:
            return event
        
@method_decorator(login_required, name='dispatch')        
class ProfileSchoolAdd(CreateView):
    """
    Добавить школу в профиле
    """
    model = School
    form_class = SchoolAddForm
    template_name = 'profiles/add_school.html'
    success_url = '/school/'
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.city = self.object.school_town.title
        self.object.save()
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=str(self.object),
            action_flag=ADDITION)
        
        return super(ProfileSchoolAdd, self).form_valid(form)

        
@method_decorator(login_required, name='dispatch')
class ProfileSchoolEdit(UpdateView):
    """
    Изменить школу в профиле
    """
    model = School
    form_class = SchoolAddForm
    template_name = 'profiles/edit_school.html'
   

    
    def get_success_url(self):
        return reverse_lazy('profiles:profile_detail',  kwargs = {'pk' : self.kwargs['pk'], })
    
    def get_object(self):
        school = get_object_or_404(School, slug=self.kwargs['slug'])  
        if self.request.user != school.user:                                              
            raise Http404()
        else:
            return school
            
@method_decorator(login_required, name='dispatch')
class ProfileSchoolEditSocial(UpdateView):
    """
    Изменить соц сети в профиле автошколы
    """
    model = School
    form_class = SchoolSocialForm
    template_name = 'profiles/edit_school_social.html'
    
    def get_success_url(self):
        return reverse_lazy('profiles:profile_detail',  kwargs = {'pk' : self.kwargs['pk'], })
    
    def get_object(self):
        school = get_object_or_404(School, slug=self.kwargs['slug'])                                      
        if self.request.user != school.user:                                              
            raise Http404()
        else:
            return school

@method_decorator(login_required, name='dispatch')
class ProfileSchoolDelete(DeleteView):
    """
    Удалить школу в профиле
    """
    model = School
    template_name = 'profiles/delete_school.html'
    def get_success_url(self):
        return reverse('profiles:profile_schools', kwargs = {'pk' : self.kwargs.get('pk')})
    def get_object(self):
        return get_object_or_404(School, slug=self.kwargs.get('slug'))        
        
@method_decorator(login_required, name='dispatch')    
class ProfileSchoolAdress(DetailView):
    """
    Филиалы и автодромы школы в профиле
    """
    model = School
    template_name = 'profiles/school_address.html'
    def get_object(self):
        return get_object_or_404(School, slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        context = super(ProfileSchoolAdress,self).get_context_data(**kwargs)
        context['branch_list'] = Branch.objects.filter(school__slug=self.kwargs['slug'])
        context['autodrome_list'] = Autodrome.objects.filter(school__slug=self.kwargs['slug'])
        return context

@method_decorator(login_required, name='dispatch')
class ProfileBranchAdd(CreateView):
    """
    Добавить адрес школы в профиле
    """
    model = Branch
    form_class = BranchEditForm
    template_name = 'profiles/add_branch.html'
    def form_valid(self,form):
        self.object = form.save(commit=False)
        school = get_object_or_404(School, slug=self.kwargs.get('slug'))
        self.object.school = school
        self.object.save()
        return super(ProfileBranchAdd, self).form_valid(form)

@method_decorator(login_required, name='dispatch')    
class ProfileBranchEdit(UpdateView):
    """
    Изменить адрес школы в профиле
    """
    model = Branch
    form_class = BranchEditForm
    template_name = 'profiles/edit_branch.html'
    def get_object(self):
        return get_object_or_404(Branch, id=self.kwargs.get('branch_pk'))
        
@method_decorator(login_required, name='dispatch')
class ProfileBranchDelete(DeleteView):
    """
    Удалить адрес школы в профиле
    """
    model = Branch
    template_name = 'profiles/delete_branch.html'
    def get_success_url(self):
        return reverse('profiles:profile_branch_list', kwargs = {'pk' : self.kwargs.get('pk'), 'slug' : self.kwargs.get('slug') })
    def get_object(self):
        return get_object_or_404(Branch, id=self.kwargs.get('branch_pk'))
        
@method_decorator(login_required, name='dispatch')
class ProfileAutodromeAdd(CreateView):
    """
    Добавить автодром школы в профиле
    """
    model = Autodrome
    form_class = AutodromeAddForm
    template_name = 'profiles/add_autodrome.html'
    def form_valid(self,form):
        self.object = form.save(commit=False)
        school = get_object_or_404(School, slug=self.kwargs.get('slug'))
        self.object.school = school
        self.object.save()
        return super(ProfileAutodromeAdd, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class ProfileAutodromeEdit(UpdateView):
    """
    Изменить автодром школы в профиле
    """
    model = Autodrome
    form_class = AutodromeAddForm
    template_name = 'profiles/edit_autodrome.html'
    def get_object(self):
        return get_object_or_404(Autodrome, id=self.kwargs.get('autodrome_pk'))
        
@method_decorator(login_required, name='dispatch')
class ProfileAutodromeDelete(DeleteView):
    """
    Удалить автодром школы в профиле
    """
    model = Autodrome
    template_name = 'profiles/delete_autodrome.html'
    def get_success_url(self):
        return reverse('profiles:profile_branch_list', kwargs = {'pk' : self.kwargs.get('pk'), 'slug' : self.kwargs.get('slug') })
    def get_object(self):
        return get_object_or_404(Autodrome, id=self.kwargs.get('autodrome_pk'))
        
@method_decorator(login_required, name='dispatch')        
class ProfileSchoolImageList(ListView):
    """
    Изображения школы в профиле
    """
    model = SchoolImage
    template_name = 'profiles/schoolimage_list.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileSchoolImageList,self).get_context_data(**kwargs)
        context['schoolimage_list'] = SchoolImage.objects.filter(school__slug=self.kwargs['slug'])
        return context

@method_decorator(login_required, name='dispatch')        
class ProfileSchoolImageAdd(CreateView):
    """
    Добавить изображения школы в профиле
    """
    model = SchoolImage
    form_class = SchoolImageAddForm
    template_name = 'profiles/add_schoolimage.html'
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        school = get_object_or_404(School, slug=self.kwargs.get('slug'))
        self.object.school = school
        self.object.save()
        return super(ProfileSchoolImageAdd, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class ProfileSchoolImageDelete(DeleteView):
    """
    Удалить автодром школы в профиле
    """
    model = SchoolImage
    template_name = 'profiles/delete_schoolimage.html'
    def get_success_url(self):
        return reverse('profiles:profile_schoolimage_list', kwargs = {'pk' : self.kwargs.get('pk'), 'slug' : self.kwargs.get('slug') })
    def get_object(self):
        return get_object_or_404(SchoolImage, id=self.kwargs.get('image_pk'))
        
        
@method_decorator(login_required, name='dispatch')        
class ProfileBillAdd(CreateView):
    """
    Добавить счет в профиле
    """
    model = Bill
    form_class = BillAddForm
    template_name = 'profiles/add_bill.html'
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ProfileBillAdd, self).form_valid(form)
        
        
@method_decorator(login_required, name='dispatch')        
class ProfileSchoolDocumentList(ListView):
    """
    Документы школы в профиле
    """
    model = SchoolDocument
    template_name = 'profiles/schooldocument_list.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileSchoolDocumentList,self).get_context_data(**kwargs)
        context['school'] = School.objects.get(slug=self.kwargs['slug'])
        context['schooldocument_list'] = SchoolDocument.objects.filter(school__slug=self.kwargs['slug'])
        return context

@method_decorator(login_required, name='dispatch')        
class ProfileSchoolDocumentAdd(CreateView):
    """
    Добавить документ школы в профиле
    """
    model = SchoolDocument
    form_class = SchoolDocumentAddForm
    template_name = 'profiles/add_schooldocument.html'
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        school = get_object_or_404(School, slug=self.kwargs['slug'])
        self.object.school = school
        self.object.save()
        return super(ProfileSchoolDocumentAdd, self).form_valid(form)    

        
@method_decorator(login_required, name='dispatch')    
class ProfileInstructors(DetailView):
    model = User
    template_name = 'profiles/profile_instructors.html'
    def get_context_data(self,**kwargs):
        context = super(ProfileInstructors, self).get_context_data(**kwargs)
        context['instructor_list'] = Instructor.objects.filter(user_id = self.object.id)
        return context
    def get_object(self):                                                      
        event = get_object_or_404(User, id=self.kwargs['pk'])                                      
        if self.request.user != event:                                              
            raise Http404()
        else:
            return event        
        
@method_decorator(login_required, name='dispatch')        
class ProfileInstructorAdd(CreateView):
    """
    Добавить интсруктора в профиле
    """
    model = Instructor
    form_class = InstructorAddForm
    template_name = 'profiles/add_instructor.html'
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.slug = slugify(unidecode(self.object.fio))
        self.object.save()
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=self.object.id,
            object_repr=str(self.object),
            action_flag=ADDITION)
        return super(ProfileInstructorAdd, self).form_valid(form)
        
@method_decorator(login_required, name='dispatch')    
class ProfileInstructorsEdit(UpdateView):
    """
    Изменить инструктора в профиле
    """
    model = Instructor
    form_class = InstructorAddForm
    template_name = 'profiles/profile_instructors_edit.html'
    def get_object(self):                                                      
        event = get_object_or_404(Instructor, id=self.kwargs['instructor_pk'])                                      
        if self.request.user != event.user:                                              
            raise Http404()
        else:
            return event  

   


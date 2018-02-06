# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Course,Path,Author
from django.contrib.auth.models import User
from .forms import UserCreateForm,CourseForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, reverse, Http404
from django.views import View
from django.conf import settings    
from django.core.mail import send_mail
from django.contrib import messages

#import pdb

# Create your views here.

class PathListView(generic.ListView):
    model = Path
    paginate_by = 10
    

    

class my_PathsListView(LoginRequiredMixin,PathListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = Author.objects.get(user=self.request.user)
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)

    def get_queryset(self):
       return Path.objects.filter(creator=self.request.user)

class AuthorPathsListView(PathListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = User.objects.get(username=self.kwargs['slug']).author
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)

    def get_queryset(self):
       return Path.objects.filter(creator=User.objects.get(username=self.kwargs['slug']))






class PathDetailView(generic.DetailView):
    model = Path

    
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = self.get_object()
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['courses'] = self.get_object().base.above.all()
        return context


#pdb.set_trace()
class PathCreate(LoginRequiredMixin,generic.CreateView):
    model = Path
    fields = ['name', 'slug', 'description','photo']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class PathUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Path
    fields = ['name', 'description','photo']

class PathDelete(UserPassesTestMixin,generic.DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().creator

    model = Path
    success_url = reverse_lazy('paths:index')






def add_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('paths:index')
    return render(request, 'paths/add_course.html', {"form": form})




class CourseListView(generic.ListView):
    model = Course
    paginate_by = 10


class CourseDetailView(generic.DetailView):
    model = Course
    
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = self.get_object()
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)


class my_CoursesListView(LoginRequiredMixin,CourseListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = Author.objects.get(user=self.request.user)
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)

    def get_queryset(self):
       return Course.objects.filter(creator=self.request.user)

class AuthorCoursesListView(LoginRequiredMixin,CourseListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = User.objects.get(username=self.kwargs['slug']).author
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)


    def get_queryset(self):
       return Course.objects.filter(creator=User.objects.get(username=self.kwargs['slug']))



#pdb.set_trace()
class CourseCreate(LoginRequiredMixin,generic.CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class CourseCreateForPath(CourseCreate):
    def get_context_data(self, **kwargs):
        path = Path.objects.get(slug = self.kwargs['slug'] )
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        context['form'].initial['path'] = path
        context['form'].fields['path'].disabled= True
        context['form'].fields['depend_on'].queryset = Course.objects.filter(path=path)
        return context


class CourseUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Course
    form_class = CourseForm

class CourseDelete(UserPassesTestMixin,generic.DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().creator

    model = Course
    success_url = reverse_lazy('paths:index')

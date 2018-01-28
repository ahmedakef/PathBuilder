# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Course,Path,Author
from django.contrib.auth.models import User
from .forms import UserCreateForm
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
    
    def get_queryset(self):
       return Path.objects.filter(creator=self.request.user)

class AuthorPathsListView(PathListView):

    def get_queryset(self):
        
       return Path.objects.filter(creator=self.kwargs['pk'])






class PathDetailView(generic.DetailView):
    model = Path
    
    
    def get_context_data(self,**kwargs):
        # Call the base implementation first to get the context
        context = super(PathDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['courses'] = [self.get_object().base]
        return context


#pdb.set_trace()
class PathCreate(LoginRequiredMixin,generic.CreateView):
    model = Path
    fields = ['name', 'description','photo']

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
    
class my_CoursesListView(LoginRequiredMixin,CourseListView):
    
    def get_queryset(self):
       return Path.objects.filter(creator=self.request.user)


#pdb.set_trace()
class CourseCreate(LoginRequiredMixin,generic.CreateView):
    model = Course
    fields = ['name', 'description','depend_on','path','photo']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class CourseUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Course
    fields = ['name', 'description','depend_on','path','photo']

class CourseDelete(UserPassesTestMixin,generic.DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().creator

    model = Course
    success_url = reverse_lazy('paths:index')

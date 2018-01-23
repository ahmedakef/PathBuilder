# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Course,Path
from .forms import CourseForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy,reverse

#import pdb

# Create your views here.

class PathListView(generic.ListView):
    model = Path
    paginate_by = 10
    

    

class my_PathsListView(PathListView):

    
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



class CourseListView(generic.ListView):
    model = Course
    paginate_by = 10



#pdb.set_trace()
class PathCreate(generic.CreateView):
    model = Path
    fields = ['name', 'description']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class PathUpdate(generic.UpdateView):
    model = Path
    fields = ['name', 'description']

class PathDelete(generic.DeleteView):
    model = Path
    success_url = reverse_lazy('paths:index')


def add_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('paths:index')
    return render(request, 'paths/add_course.html', {"form": form})

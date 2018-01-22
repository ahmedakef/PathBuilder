# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Course,Path
from .forms import CourseForm,PathForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views import generic

#import pdb

# Create your views here.

class PathListView(generic.ListView):
    model = Path
    paginate_by = 10
    
    def get_queryset(self):
        return Path.objects.all()[:5]
    




def my_paths(request):
    paths = Path.objects.filter(creator=request.user)
    return render(request, 'paths/paths.html', {'paths': paths})


class PathDetailView(generic.ListView):
    model = Path
    

    
    def get_context_data(self,**kwargs):
        # Call the base implementation first to get the context
        context = super(PathDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['courses'] = base
        return context



def show_path(request,path_id):

    path = get_object_or_404(Path, pk=path_id)
    base = [path.base]
    context = {
        'courses': base,
        'path': path
    }


def courses(request):

    courses = Course.objects.all()

    return render(request, 'paths/index.html', {'courses': courses})



    return render(request, 'paths/show_path.html', context)

#pdb.set_trace()
def edit_path(request,path_id):
    path = Path.objects.get(pk=path_id)
    form = PathForm(request.POST or None,instance = path)
    #assert (request.method == "GET")
    if form.is_valid():
        form.save()
        return redirect('paths:index')
    #form = PathForm(instance= path )
    return render(request, 'paths/edit_path.html', {"form": form,"Path_id":path_id})



def add_path(request):
    form = PathForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('paths:index')
    return render(request, 'paths/add_path.html', {"form": form})


def add_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('paths:index')
    return render(request, 'paths/add_course.html', {"form": form})

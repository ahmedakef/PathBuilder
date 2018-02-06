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



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500)
    depend_on = models.ManyToManyField('self',related_name="above", blank=True,symmetrical=False)
    path = models.ForeignKey('Path', null=True,blank=True , on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)  
        
    def __str__(self):
        return self.name

class Path(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500)
    base = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="base",blank=True,null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('paths:show_path',args=[str(self.id)])

    def __str__(self):
        return self.name

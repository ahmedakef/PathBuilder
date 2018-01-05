# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500)
    depend_on = models.ManyToManyField('self',related_name="above", blank=True,symmetrical=False)
    path = models.ForeignKey('Path', null=True,blank=True , on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Path(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500)
    base = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="base",blank=True)

    def __str__(self):
        return self.name

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



def get_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/modelname/<filename>
    return '{0}/{1}'.format(instance.__class__.__name__, filename)




dummyimage = 'dummyimage.png'

class Course(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200 , unique=True,null=False,blank=False)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=400,blank=True)
    depend_on = models.ManyToManyField('self',related_name="above", blank=True,symmetrical=False)
    path = models.ForeignKey('Path', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(default= dummyimage ,blank= True,upload_to=get_directory)
    access_counter = models.IntegerField(default=0, verbose_name="Access Counts")

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)  
        ordering = ["-access_counter"]

    def save(self, *args, **kwargs):
        if self.photo == '':
            self.photo = dummyimage
        super().save(*args, **kwargs)  # Call the "real" save() method.




    def get_absolute_url(self):
        return reverse('paths:show_course',args=[str(self.slug)])

    def __str__(self):
        return self.name



class Path(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200 , unique=True,null=False,blank=False)

    description = models.CharField(max_length=500)
    base = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="base",blank=True,null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(default= dummyimage ,blank= True,upload_to=get_directory)
    access_counter = models.IntegerField(default=0, verbose_name="Access Counts")


    def save(self, *args, **kwargs):
        if self.photo == '':
            self.photo = dummyimage
        
        created = self.pk is None
        super().save(*args, **kwargs)  # Call the "real" save() method.
        if created:
            baseCourse_params = {
                'name' : "base {0}".format(self.name),
                'slug' : self.slug+"-Base",
                'description' : "just hidden base course to build upon for {0}".format(self.name),
                'path' : self,
                'creator' : self.creator
            }
            base_Course = Course.objects.create(**baseCourse_params)
            self.base = base_Course
            self.save()  # Call the "real" save() method.

    
    class Meta:
        ordering = ["-access_counter"]



    def get_absolute_url(self):
        return reverse('paths:show_path',args=[str(self.slug)])

    def __str__(self):
        return self.name

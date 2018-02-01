# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def get_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/modelname/<filename>
    return '{0}/{1}'.format(instance.__class__.__name__, filename)



class Author(models.Model):
    ## required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200 ,unique=True,null=False,blank=False)

    ## additional fields
    phone = models.IntegerField(blank=True, default=1)    
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author_paths', args=[self.slug])



dummyimage = 'dummyimage.png'

class Course(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200 , unique=True,null=False,blank=False)
    description = models.CharField(max_length=500)
    depend_on = models.ManyToManyField('self',related_name="above", blank=True,symmetrical=False)
    path = models.ForeignKey('Path', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(default= dummyimage ,blank= True,upload_to=get_directory)

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)  

    def save(self, *args, **kwargs):
        if self.photo == '':
            self.photo = dummyimage
        super().save(*args, **kwargs)  # Call the "real" save() method.
        if not self.depend_on.exists() :
            print(self.depend_on.all())
            self.depend_on.add(self.path.base)
        #    print(self.path.base)
            print(self.depend_on.all())
        #super().save(*args, **kwargs)  # Call the "real" save() method.



    def get_absolute_url(self):
        return reverse('paths:show_course',args=[str(self.slug)])

    def __str__(self):
        return self.name


from django.utils.text import slugify

class Path(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200 , unique=True,null=False,blank=False)

    description = models.CharField(max_length=500)
    base = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="base",blank=True,null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(default= dummyimage ,blank= True,upload_to=get_directory)

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
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def get_absolute_url(self):
        return reverse('paths:show_path',args=[str(self.slug)])

    def __str__(self):
        return self.name

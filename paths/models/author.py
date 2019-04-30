# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Author(models.Model):
    ## required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)

    ## additional fields
    phone = models.IntegerField(blank=True, default=1)    
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    access_counter = models.IntegerField(default=0, verbose_name="Access Counts")
    
    class Meta:
        ordering = ["-access_counter"]


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('paths:author_paths', args=[self.user.username])


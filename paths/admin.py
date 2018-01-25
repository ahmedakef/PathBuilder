# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Course,Path,Author
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Course)
admin.site.register(Path)

# Define an inline admin descriptor for Author model
# which acts a bit like a singleton
class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    verbose_name_plural = 'author'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
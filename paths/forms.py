from django import forms
from django.contrib.auth.models import User

from .models import Course,Path

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


    def clean_email(self):
        """
        Validate that the supplied email address is unique.
        """
        print("a77777a")
        email = self.cleaned_data['email']
        r = User.objects.filter(email__iexact=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    


    #def save(self,commit=True):
    #    user = super(UserCreateForm,self).save(commit=False)
    #    
    #    if commit:
    #        user.save()
    #    return user


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'slug','description','path','depend_on','photo']


    def clean_depend_on(self):
        """
        if depend_on is empty assign it to the base course of the path.
        """
        depend_on = self.cleaned_data['depend_on']
        if not depend_on.exists():
            depend_on = [self.cleaned_data['path'].base]

        return depend_on

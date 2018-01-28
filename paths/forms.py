from django import forms
from django.contrib.auth.models import User

from .models import Course,Path




from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


    def clean_email(self):
        """
        Validate that the supplied email address is unique.
        """

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
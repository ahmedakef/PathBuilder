from django import forms
from django.contrib.auth.models import User

from .models import Course,Path


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'description','depend_on','path']

class PathForm(forms.ModelForm):

    class Meta:
        model = Path
        fields = ['name', 'description']

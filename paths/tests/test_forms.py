# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from paths.forms import CourseForm,UserCreateForm
from django.contrib.auth.models import User
from paths.models import Course,Path,Author


# Create your tests here.


class UserFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="ali",email="ali@PathBuilder.com")

    def test_create_wuth_existing_email(self):
        form_data = {'email':'ali@PathBuilder.com'}
        form = UserCreateForm(data = form_data)
        self.assertFalse(form.is_valid())


# bug

# class CourseFormTest(TestCase):

#     @classmethod
#     def setUp(self):
#         path = Path.objects.create(name="physics")


#     def test_depend_on_empty(self):
#         path = Path.objects.get(id=1)
#         form_data = {'depend_on':[],'path':path}
#         form = CourseForm(data=form_data)
#         self.assertTrue(form.is_valid())

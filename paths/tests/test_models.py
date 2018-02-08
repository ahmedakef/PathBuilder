# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from paths.models import Course,Path,Author
from django.contrib.auth.models import User

# Create your tests here.

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="ali")

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(),'/paths/author/ali/')
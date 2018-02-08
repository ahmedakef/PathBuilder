# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from paths.models import Course,Path,Author
from django.urls import reverse
from django.contrib.auth.models import User

class PathListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 paths for pagination tests
        number_of_paths = 13
        for path_num in range(number_of_paths):
            Path.objects.create(name='Path %s' % path_num,slug='path-%s' % path_num)
           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/paths/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paths:index'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paths:index'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'paths/path_list.html')
        
    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('paths:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['path_list']) == 10)

    def test_lists_all_paths(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('paths:index')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['path_list']) == 3)



class PathEditViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345') 
        test_user2.save()
        
        test_path1 = Path.objects.create(name="CS",slug="CS",creator=test_user1)
        test_path2 = Path.objects.create(name="ACC",slug="ACC",creator=test_user2)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('paths:my_paths'))
        self.assertRedirects(resp, '/accounts/login?next=/paths/my_paths/',fetch_redirect_response=False)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('paths:my_paths'))
        
        #Check our user is logged in
        self.assertEqual(str(resp.context['user']), 'testuser1')
        #Check that we got a response "success"
        self.assertEqual(resp.status_code, 200)

        #Check we used correct template
        self.assertTemplateUsed(resp, 'paths/path_list.html')


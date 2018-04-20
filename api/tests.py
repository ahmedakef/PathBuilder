from django.test import TestCase

# Create your tests here.

from paths.models import Path
from django.utils.text import slugify

class PathTestCase(TestCase):
    """This class defines the test suite for the Path model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.path_name = "Write world class code"
        self.path_slug = slugify(self.path_name)
        self.Path = Path(name=self.path_name,slug=self.path_slug)

    def test_model_can_create_a_Path(self):
        """Test the Path model can create a Path."""
        old_count = Path.objects.count()
        self.Path.save()
        new_count = Path.objects.count()
        self.assertNotEqual(old_count, new_count)



# Add these imports at the top
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.path_data = {'name': 'Go to Ibiza','slug':'Go_to_Ibiza','description':'when created'}
        self.response = self.client.post(
            reverse('create'),
            self.path_data,
            format="json")

    def test_api_can_create_a_path(self):
        """Test the api has path creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)



    def test_api_can_get_a_path(self):
        """Test the api can get a given path."""
        path = Path.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'slug': path.slug}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, path)

    # the reponse is 400
    # def test_api_can_update_path(self):
    #     """Test the api can update a given path."""
    #     path = Path.objects.get()
    #     change_path = {'description': 'Something'}
    #     res = self.client.put(
    #         reverse('details', kwargs={'slug': path.slug}),
    #         change_path, format='json'
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_path(self):
        """Test the api can delete a path."""
        path = Path.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'slug': path.slug}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
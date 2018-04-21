from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author,Path,Course
from PathBuilder.helpers import send_activation_key

from rest_framework.authtoken.models import Token




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
        send_activation_key(instance)
        # This receiver handles token creation immediately a new user is created.
        Token.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.Author.save()


# another approach for creating base course when creating path using signals

# @receiver(post_save, sender=Path)
# def create_user_profile(sender, instance, created, **kwargs):

#     if created:
#         baseCourse_params = {
#             'name' : "base {0}".format(instance.name),
#             'slug' : instance.slug+"-Base",
#             'description' : "just hidden base course to build upon for {0}".format(instance.name),
#             'path' : instance,
#             'creator' : instance.creator
#         }
#         base_Course = Course.objects.create(**baseCourse_params)
#         instance.base = base_Course
#         instance.save()


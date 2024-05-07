from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        models.Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

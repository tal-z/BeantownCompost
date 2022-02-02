from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ManagerProfile
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def create_managerprofile(sender, instance, created, **kwargs):
    if created:
        ManagerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_managerprofile(sender, instance, **kwargs):
    try:
        instance.managerprofile.save()
    except ObjectDoesNotExist:
        ManagerProfile.objects.create(user=instance)


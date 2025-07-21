from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for storing user information and delivery details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    street_address1 = models.CharField(max_length=80, blank=True, null=True)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile automatically on user creation or update.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

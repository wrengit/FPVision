from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, blank=False, null=True
    )
    default_country = CountryField(
        blank_label="Country *", blank=False, null=True
    )
    default_postcode = models.CharField(max_length=20, blank=False, null=True)
    default_post_town = models.CharField(max_length=40, blank=False, null=True)
    default_address_1 = models.CharField(max_length=80, blank=False, null=True)
    default_address_2 = models.CharField(max_length=80, blank=False, null=True)
    default_county = models.CharField(max_length=80, blank=False, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

from django.db import models


class ContactList(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    date_time = models.DateTimeField(auto_now_add=True)

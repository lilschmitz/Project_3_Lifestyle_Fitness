from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="images", blank=True, null=True)


    def __unicode__(self):
        return self.user
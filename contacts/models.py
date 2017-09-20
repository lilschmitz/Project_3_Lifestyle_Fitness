from __future__ import unicode_literals

from django.db import models
# from django.utils import timezone

# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="images", blank=True, null=True)


    @property
    def bmi(self):
        height_meters = self.height / float(100)
        bmi = self.weight / (height_meters * height_meters)
        return round(bmi, 2)

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
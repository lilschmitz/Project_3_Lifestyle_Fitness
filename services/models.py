
from __future__ import unicode_literals

from django.db import models


from django.conf import settings

class Video(models.Model):
    video = models.FilePathField(path=settings.MEDIA_ROOT)

class Service(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)


    def __unicode__(self):
        return self.name



from __future__ import unicode_literals

from django.db import models
from services.models import Service
from django.contrib.auth.models import User


# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User)
    service = models.ForeignKey(Service)
    quantity = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.service.name, self.quantity)
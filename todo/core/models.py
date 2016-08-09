from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.
class todo(models.Model):
    naam = models.CharField(max_length=75, unique=True)
    beschrijving = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.naam

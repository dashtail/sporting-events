# enconding: utf-8

from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField()

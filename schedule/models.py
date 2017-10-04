# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Show(models.Model):
    pbs_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.title

class Season(models.Model):
    show = models.ForeignKey(Show)
    pbs_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    ordinal = models.IntegerField(default=0)

    def __str__(self):
        return 'season '+str(self.ordinal)+' of '+str(self.show)

class Collection(models.Model):
    show = models.ForeignKey(Show)
    pbs_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.title

class Episode(models.Model):
    pbs_id = models.CharField(max_length=200)
    season = models.ForeignKey(Season, blank=True, null=True)
    collection = models.ForeignKey(Collection, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    ordinal = models.IntegerField(default=0)
    premiered_on = models.DateField(blank=True, null=True)
    encored_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

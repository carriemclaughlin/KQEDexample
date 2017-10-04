# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels
from django.conf import settings
import logging
import requests
import urllib

logger = logging.getLogger(__name__)


class Film(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(default=0)
    production_company = models.CharField(max_length=200)
    distributor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{} ({})'.format(self.title, self.release_year)


class FilmLocation(gismodels.Model):
    film = gismodels.ForeignKey(Film)
    name = gismodels.CharField(max_length=200)
    address = gismodels.CharField(max_length=200)
    location = gismodels.PointField(null=True, blank=True)
    fun_facts = gismodels.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.address

    def save(self, *args, **kwargs):
        from django.contrib.gis.geos import Point
        import requests # use google API to get lat long when address saved.
        if self.location == None:
            if isinstance(self.address, str):
                address = unicode(self.address,'utf8') + u' SF'
            address = address.encode('utf8')
            r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+urllib.quote_plus(address)+'&key='+settings.GOOGLE_AUTH)
            json = r.json()
            try:
                self.location = Point(json['results'][0]['geometry']['location']['lng'], json['results'][0]['geometry']['location']['lat'])
                self.address = json['results'][0]['formatted_address']
            except IndexError:
                logger.error(u'google could not find location for address '+address)
        super(FilmLocation, self).save(*args, **kwargs) # Call the "real" save() method.


class FilmActor(models.Model):
    film = models.ForeignKey(Film)
    actor = models.CharField(max_length=200)

    def __unicode__(self):
        return self.actor
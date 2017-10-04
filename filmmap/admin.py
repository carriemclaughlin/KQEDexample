# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from filmmap.models import Film, FilmLocation, FilmActor


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title','release_year','production_company','director','distributor','writer')
admin.site.register(Film, FilmAdmin)

class FilmLocationAdmin(admin.ModelAdmin):
    list_display = ('film','address','location')
    list_editable = ['address',]
admin.site.register(FilmLocation, FilmLocationAdmin)

class FilmActorAdmin(admin.ModelAdmin):
    list_display = ('film','actor')
admin.site.register(FilmActor, FilmActorAdmin)

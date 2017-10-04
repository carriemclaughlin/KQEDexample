# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from schedule.models import Show, Season, Collection, Episode

admin.site.register(Show)
admin.site.register(Season)
admin.site.register(Collection)
admin.site.register(Episode)
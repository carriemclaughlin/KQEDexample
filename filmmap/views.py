# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    """This page is for finding SF film locations"""
    from django.contrib.gis.measure import D
    from django.contrib.gis.geos import Point
    import urllib

    return render(request, 'filmmaps/index.html', {})

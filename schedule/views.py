# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

import requests

def index(request):

    
    station = request.COOKIES.get('station', None)
    if request.GET.get('zipcode', None) != None:
        station = requests.get('http://services.pbs.org/callsigns/zip/'+request.GET.get('zipcode', None)+'.json', auth=settings.PBS_AUTH)
        if station.status_code == 200:
            station = station.json()['$items'][0]['$links'][0]['callsign']
        else:
            station = None
    if station == None or station == 'None':
        ip = request.META['REMOTE_ADDR']
        zipcode = requests.get('http://services.pbs.org/zipcodes/ip/'+ip+'.json', auth=settings.PBS_AUTH)
        if zipcode.status_code == 200:
            zipcode = zipcode.json()['$items'][0]['zipcode']
            station = requests.get('http://services.pbs.org/callsigns/zip/'+zipcode+'.json', auth=settings.PBS_AUTH)
            if station.status_code == 200:
                print station.json()['$items'][0]['$links'][0]['callsign']
                station = station.json()['$items'][0]['$links'][0]['callsign']
            else:
                station = None

    response = render(request, 'schedule/index.html', {'station':station})
    response.set_cookie('station', station)
    return response

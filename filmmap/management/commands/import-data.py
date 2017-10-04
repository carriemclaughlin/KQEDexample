from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from filmmap.models import Film, FilmLocation, FilmActor

from decimal import *
import re
import csv
from datetime import datetime


class CSVParser(object):
    def __init__(self, filename):
        self.infile = open(filename, "r")
        self.reader = csv.reader(self.infile)
        self.got_header = False

    def readlines(self):
        for row in self.reader:
            if not self.got_header:
                self.got_header = True
                continue
            else:
                if row != "":
                    yield row

    def close(self):
        self.infile.close()


class Command(BaseCommand):
    help = 'Imports film location data into database.'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        # Columns of csv file are: 
        # 0. Title
        # 1. Release year
        # 2. location
        # 3. fun facts
        # 4. production company
        # 5. distributor
        # 6. writer
        # 7. actor 1
        # 8. actor 2
        # 9. actor 3

        parser = CSVParser(options['file'][0])
        for row in parser.readlines():
            self.stdout.write("Title: "+row[0])
            self.stdout.write("Release year: "+row[1])
            film, created = Film.objects.get_or_create(title=row[0], release_year=row[1])
            if created:
                film.production_company = row[4]
                film.distributor = row[5]
                film.writer = row[6]
                film.save()

            if row[7] != None and row[7] != '':
                actor, created1 = FilmActor.objects.get_or_create(film=film, actor=row[7])
            if row[8] != None and row[8] != '':
                actor2, created2 = FilmActor.objects.get_or_create(film=film, actor=row[8])
            if row[9] != None and row[9] != '':
                actor3, created3 = FilmActor.objects.get_or_create(film=film, actor=row[9])

            film_location, location_created = FilmLocation.objects.get_or_create(film=film, name=row[2], fun_facts=row[3], defaults={'address':row[2]})
        parser.close()


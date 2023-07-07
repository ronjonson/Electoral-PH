import pandas as pd
from django.core.management.base import BaseCommand
from electoral.models import *
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "a command to add data from an excel file to the database"

    def add_arguments(self, parser):
        parser.add_argument('-f','--filename', type=str, help='file name of the file to be opened')
        parser.add_argument('-s', '--sheet', type=str, help='sheetname of the file')
        parser.add_argument('-d', '--database', type=str, help='database name')

    def handle(self, *args, **kwargs):
        
        filename = kwargs['filename']
        sheetname = kwargs['sheet']
        database = kwargs['database']

        df = pd.read_excel(f'data/{filename}.xlsx', sheetname)
        for 
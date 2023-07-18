import pandas as pd
from django.core.management.base import BaseCommand
from electoral.models import *
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "a command to add data from an excel file to the database"

    def add_arguments(self, parser):
        parser.add_argument('-f','--filename', type=str, help='file name of the file to be opened')
        parser.add_argument('-s', '--sheet', type=str, help='sheetname of the file')

    def handle(self, *args, **kwargs):
        
        filename = kwargs['filename']
        sheetname = kwargs['sheet']

        df = pd.read_excel(f'data/{filename}.xlsx', sheetname)
        #engine = create_engine('sqlite:///db.sqlite3')
        #df.to_sql(eval(f"{database}._meta.db_table"), if_exists='replace', con=engine, index=False)

        for i, row in df.iterrows():
            p = Candidate.objects.create(
                candidate = row['candidate'],
                full_name = row['full_name']
            )
            p.save()

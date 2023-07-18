from electoral.models import *
from django.core.management.base import BaseCommand
from django_pandas.io import read_frame
from django.db.models import Sum

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


PROVINCES = "data\provinces-svg.txt"
COLORS = "data\colors.csv"

class Command(BaseCommand):
    help = "just testing out some utils"

    def add_arguments(self, parser):
        parser.add_argument('-f','--filename', type=str, help='file name of the file to be opened')
    def handle(self, *args, **kwargs):
        #filename = kwargs['filename']

        qs = Pres_2004.objects.all()
        df = read_frame(qs)
        df = df.drop(columns=['id'])
        df = df.set_index('province')
        a = df.to_dict('index')
        #Candidate.objects.filter(candidate=candidate).values_list('full_name')[0][0]
        #for key, values in a.items():
        #key = 'Abra'
        #print(a[key])
        #print(sorted(a[key], key=a[key].get, reverse=True))
        ranked_votes = {}
        for k, v in a.items():
            ranked = sorted(v, key= v.get, reverse=True)
            votes = []
            for rank in ranked:
                votes.append(
                    [Candidate.objects.filter(candidate=rank).values_list('full_name')[0][0], v[rank]]
                )
            ranked_votes.update({k: votes})
            print(ranked_votes)
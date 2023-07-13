import pandas as pd

from django_pandas.io import read_frame
from django.db.models import Sum

from .models import *

PROVINCES = "data\provinces-svg.txt"
COLORS = "data\colors.csv"

def get_provinces():
    df = pd.read_csv(PROVINCES, sep=':')
    return pd.Series(df.svg.values, index=df.province).to_dict()

def get_colors(year):
    df = pd.read_csv(COLORS)
    year_df = df.loc[df['year'] == year]
    return pd.Series(year_df.color.values, index=year_df.candidate).to_dict()

def get_electors(year):
    qs = eval(f'Reps_{year}.objects.all()')
    df = read_frame(qs)
    return pd.Series(df.electors.values, index=df.province).to_dict()

def get_total(candidate,position,year):
    obj = eval(f'{position}_{year}.objects')
    return obj.aggregate(Sum(candidate))[f'{candidate}__sum']
    

def closest(K, lst = [0, 0.25, 0.5, 0.75]):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def get_percentages(points):
    total = sum(points.values())
    percentages = {}
    
    for key, value in points.items():
        percentages.update({
                    key: round((value/total)*100)
        })

    return percentages
        
def total_to_dict(candidate_list, year, position, points, percentages, colors):
    totals = []
    for candidate in candidate_list:
        totals.append({
            'candidate': candidate,
            'votes': f"{get_total(candidate, position, year):,}",
            'points': points[candidate],
            'percentage': percentages[candidate],
            'color': colors[candidate]
        })

    return totals

def get_winner(model, year):
    qs = eval(f'{model}.objects.all()')
    df = read_frame(qs)
    df = df.drop(['id'], axis=1).set_index('province')
    winner = df.idxmax(axis=1).to_dict()

    electors = get_electors(year)

    points = {}
    for key, value in winner.items():
        elector_num = int(electors[key])
        if value in points.keys():
            points[value] += elector_num
        else:
            points.update({
                value: elector_num
            })

    return winner, points

def get_province_info(year, position):
    qs = eval(f'{position}_{year}.objects.all()')
    df = read_frame(qs)
    df = df.drop(columns=['id'])
    df = df.set_index('province')
    dict_df = df.to_dict('index')
    
    ranked_votes = {}

    for k, v in dict_df.items():
        ranked = sorted(v, key= v.get, reverse=True)
        votes = []
        for rank in ranked:
            votes.append(
                [rank, f"{v[rank]:,}"]
            )
        ranked_votes.update({k: votes})
    
    return ranked_votes


def zip_up(winners, colors, provinces):
    map = []
    for key, value in winners.items():
        province = {
            key: {
                'candidate': value,
                'color': colors[value],
                'svg': provinces[key]
            }
        }
        map.append(province)

    return map    

def get_candidates():
    qs = Candidate.objects.all()
    df = read_frame(qs)
    return pd.Series(df.full_name.values, index=df.candidate).to_dict()

def get_all_data(year, position):
    electors = get_electors(year)
    candidates =get_candidates()
    provinces = get_provinces()
    colors = get_colors(year)
    winners, points = get_winner(f'{position}_{year}', year)
    percentages = get_percentages(points)
    ranked = sorted(points, key=points.get, reverse=True)

    #get all info for the thing on top of the map whatever thats called
    ranked_totals = total_to_dict(ranked, year, position, points, percentages, colors)

    #get information per province (votes per candidate per province) for the tooltip
    ranked_votes = get_province_info(year, position)

    total_electoral_points = sum(points.values())

    # get all info for the map
    maps = zip_up(winners, colors, provinces)

    return maps, points, ranked_totals,total_electoral_points, total_electoral_points//2, ranked_votes, colors, candidates, electors


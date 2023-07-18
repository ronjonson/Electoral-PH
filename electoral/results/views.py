from django.shortcuts import render
from django.http import HttpResponse

from . import util

def index(request):
    return render(request, "results/index.html")

def result_2004(request):

    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(2004, 'Pres')

    return render(request, "results/election.html", {
        'year': 2004,
        'maps': maps,
        'points': points,
        'colors': colors,
        'candidates': candidates,
        'electors': electors,
        'ranked': ranked_totals,
        'ranked_votes': ranked_votes,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })

def result_Pres_2010(request):

    year = 2010
    position = 'Pres'

    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(year, position)

    return render(request, "results/election.html", {
        'year': year,
        'maps': maps,
        'points': points,
        'colors': colors,
        'candidates': candidates,
        'electors': electors,
        'ranked': ranked_totals,
        'ranked_votes': ranked_votes,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })

def result_VicePres_2010(request):

    year = 2010
    position = 'VicePres'

    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(year, position)

    return render(request, "results/election.html", {
        'year': year,
        'maps': maps,
        'points': points,
        'colors': colors,
        'candidates': candidates,
        'electors': electors,
        'ranked': ranked_totals,
        'ranked_votes': ranked_votes,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })

def result_Pres_2016(request):
    year = 2016
    position = 'Pres'
    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(year, position)

    return render(request, "results/election.html", {
        'year': year,
        'maps': maps,
        'points': points,
        'colors': colors,
        'candidates': candidates,
        'electors': electors,
        'ranked': ranked_totals,
        'ranked_votes': ranked_votes,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })


def result_VicePres_2016(request):
    year = 2016
    position = 'VicePres'
    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(year, position)

    return render(request, "results/election.html", {
        'year': year,
        'maps': maps,
        'points': points,
        'colors': colors,
        'candidates': candidates,
        'ranked': ranked_totals,
        'ranked_votes': ranked_votes,
        'electors': electors,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })

def result_Pres_2022(request):
    year = 2022
    position = 'Pres'
    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(year, position)
    return render(request, "results/election.html", {
        'year': year,
        'maps': maps,
        'points': points,
        'ranked': ranked_totals,
        'colors': colors,
        'electors': electors,
        'candidates': candidates,
        'ranked_votes': ranked_votes,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })
def result_VicePres_2022(request):
    year = 2022
    position = 'VicePres'
    maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(year, position)

    return render(request, "results/election.html", {
        'year': year,
        'maps': maps,
        'points': points,
        'ranked': ranked_totals,
        'colors': colors,
        'electors': electors,
        'candidates': candidates,
        'ranked_votes': ranked_votes,
        'total_electoral_points': total_electoral_points,
        'winning_electoral_points': winning_electoral_points
    })
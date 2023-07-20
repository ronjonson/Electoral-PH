from django.shortcuts import render
from django.views.generic import TemplateView

from . import util

class IndexView(TemplateView):
    template_name = 'electoral/index.html'



class ResultView(TemplateView):
    template_name="electoral/election.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        maps, points, ranked_totals,total_electoral_points, winning_electoral_points, ranked_votes, colors, candidates, electors = util.get_all_data(kwargs["year"], kwargs["position"])

        context["year"] = kwargs["year"]
        context["maps"] = maps
        context["points"] = points
        context["ranked"] = ranked_totals
        context["total_electoral_points"] = total_electoral_points
        context["winning_electoral_points"] = winning_electoral_points
        context["ranked_votes"] = ranked_votes
        context["colors"] = colors
        context["candidates"] = candidates
        context["electors"] = electors
                
        return context
from django.shortcuts import render
from django.http import HttpResponse

from . import util

def index(request):
    provinces = util.get_provinces()
    return render(request, "electoral/index.html", {
        "provinces": provinces
    })


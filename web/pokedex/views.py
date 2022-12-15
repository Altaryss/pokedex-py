from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request, optional_parameter=''):
    res = requests.get('https://pokeapi.co/api/v2/pokemon?limit=500&offset=0').json()
    parsed = res['results'][0]['url'].split('/')
    newRes = []
    for i in res['results']:
        newRes.append({
            "id": i['url'].split('/')[6],
            "data": i
        })
        
    return render(request, 'index.html', {'res': newRes})

def pokemon(request, id):
    res = requests.get('https://pokeapi.co/api/v2/pokemon/' + id).json()

    return render(request, 'pokemon.html', {'res': res})


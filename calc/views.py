#from django.http.response import HttpResponse#
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render 
import requests
from requests.api import request
from .forms import forms





# Create your views here.
# TASK 2 STARTED
# def home(request):
#     url=f'https://pokeapi.co/api/v2/type'
#     response=requests.get(url)
#     data=response.json()
#     results=data['results']
#     context = {
#        'results':results
#    }
#     return render(request,'home.html',context)

# TASK 2 ENDED

def typefetcher(request):
    url=f'https://pokeapi.co/api/v2/pokemon'
    response=requests.get(url)  
    data=response.json() 
    results=data['results']
    context={
        'results':results
    }
    return render(request,'home.html',context)

def search(request):
    url=f' https://pokeapi.co/api/v2/pokemon/1'
    find=requests.get(url)
    y=find.json()
    abilities=y['abilities']

    return render(request,'home.html',{'abilities':abilities})
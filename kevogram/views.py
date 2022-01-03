"""Kevogram views"""

from django.http import HttpResponse

#Utilities
from datetime import datetime
import pdb
from django.http import response
import json

from django.http.response import JsonResponse



def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")   
    return HttpResponse ("Hello World! the current server time is: {now}".format(now=str(now)))

def sort_integers(request):
    """This sort integers given in the path"""
    numbers=request.GET['numbers']
    list_numbers = list(numbers.split(",")) #divide los strings con comas y los almacena en una lista
    list_numbers = list(map(int, list_numbers)) #conveirte la lista de strings en enteros
    list_numbers.sort() #ordena la lista
    
    return HttpResponse(json.dumps(list_numbers)) #retorna json```


def say_hi(request, name, age):
    """Return a greeting"""
    if age<15:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hola, {} ! Welcome to kevogram'.format(name)
    return HttpResponse (message)
from django.shortcuts import render
from django.http import HttpResponse
from numpy import character
import random

# Create your views here.

def index(request):
    return render(request, 'generator/index.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789') 
    if request.GET.get('specialchars'):
        characters.extend('~@#$%^&*()`')

    length=int(request.GET.get('length',12))

    thepassword=''

    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')    
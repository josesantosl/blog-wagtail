from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo
def index(request):
    articoli= Articolo.objects.all().count()

def articolo(request):
    pass


from django.shortcuts import render
from django.http import HttpResponse

# Create your first views here.

def index(request):
    return HttpResponse("Hallo, Welt! Konichiwa!! Estas viendo el index de pools.")

def detail(request, question_id):
    return HttpResponse("Estas mirando las pregunta %s." % question_id)

def results(request, question_id):
    response = "Estas mirando los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Usted esta votando por la pregunta %s." % question_id)

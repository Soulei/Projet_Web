from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question


def index():
    template_name = 'templates/rootsapp/index.html'
    return render(request, 'template_name)

#Permet de gérer le portraits d'une personne
def portrait():

#Permet de poster un commentaire
def comment():

#Permet de consulter son profil
def profil():

#Permet de consulter son profil, les portraits tag en favoris
def favoris():

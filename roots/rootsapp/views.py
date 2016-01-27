from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

#Permet de gérer le portraits d'une personne
def portrait():

#Permet de poster un commentaire
def comment():

#Permet de consulter son profil
def profil():

#Permet de consulter son profil, les portraits tag en favoris
def favoris():

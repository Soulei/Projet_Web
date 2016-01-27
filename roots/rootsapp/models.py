from django.db import models
from django.contrib.auth.models import User


class Personne(models.Model):
    image = models.ImageField()
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField()
    date_mort = models.DateField(null=True)
    description = models.TextField()
    faits = models.TextField()
    fonctions = models.TextField()
    oeuvres = models.ManyToManyField(Oeuvre)

class Oeuvre(models.Model):
    titre = models.CharField(max_length=50)
    date_parution = models.DateField()

        
class UserProfile(models.Model):
    
    


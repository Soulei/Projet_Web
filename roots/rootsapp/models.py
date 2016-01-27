from django.db import models
from django.contrib.auth.models import User


class Personne(models.Model):
    image = 
    date_naissance = 
    date_mort = 
    description = 
    faits = 
    fonctions = 
    oeuvres = 
        
class UserProfile(models.Model):
    url = models.URLField()
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=30)
    mail_adresse = models.EmailField()
    favoris = models.ManyToManyField(Personne)
    user = models.ForeignKey(User, unique=True)
    
    def __str__(self):
        return "%s %s" % (self.pseudo, self.mail_adresse)

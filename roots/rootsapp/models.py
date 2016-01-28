from django.db import models
from django.contrib.auth.models import User

class Oeuvre(models.Model):
    titre = models.CharField(max_length=50)
    date_parution = models.DateField()

class Personne(models.Model):
    image = models.ImageField(upload_to="/portrait")
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField()
    date_mort = models.DateField(null=True)
    description = models.TextField()
    faits = models.TextField()
    fonctions = models.TextField()
    oeuvres = models.ManyToManyField(Oeuvre)
    #ajouteePar = models.ForeignKey(UserProfile, unique=True)
    nbrFavoris = models.IntegerField(default=0)
    nbrCommentaire = models.IntegerField(default=0)

def get_image_path(instance, filename):
    return os.path.join('avatar', str(instance.id), filename)
        
class UserProfile(models.Model):
    url = models.URLField()
    avatar = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=30)
    mail_adresse = models.EmailField()
    favoris = models.ManyToManyField(Personne)
    user = models.OneToOneField(User, unique=True)

    def __str__(self):
        return "%s %s" % (self.pseudo, self.mail_adresse)

class Commentaire(models.Model):
	commentaire = models.TextField()
	pseudo = models.OneToOneField(Personne, on_delete=models.CASCADE, primary_key=True)

from django import forms
from .models import Portraits, Commentaire, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import *

class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

class PortraitsForm(forms.ModelForm):
    class Meta:
        model = Portraits
        fields = ('photo', 'nom','prenom','date_naissance','date_mort','description','faits','fonctions','oeuvres', 'citations',)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('texte',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)
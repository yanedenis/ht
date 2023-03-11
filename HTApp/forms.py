from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Genre, Movie

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('__all__')

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('__all__')
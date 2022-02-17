from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Album, Musica


class NovoAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('nome_album', 'genero_album', 'logo_album')


class NovaMusicaForm(forms.ModelForm):

    class Meta:
        model = Musica
        fields = ('nome_musica', 'arquivo_musica')
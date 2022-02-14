import os
import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from imusic.settings import MEDIA_ROOT

# Função que indica o caminho do diretório do usuário
def user_directory_path(self, filename):
    # Arquivo será carregado para MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.artista_album.id, filename)


# Função que indica o caminho do diretório do usuário da música
def user_directory_path_song(self, filename):
    # Arquivo será carregado para MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_musica.artista_album.id, filename)


# Create your models here.
class Album(models.Model):
    nome_album = models.CharField(max_length=30)
    carregado_em = models.DateField(default=django.utils.timezone.now)
    logo_album = models.FileField(upload_to=user_directory_path)
    genero_album = models.CharField(max_length=30)
    artista_album = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albuns')

    def __str__(self):
        return self.nome_album

    def delete_media(self):
        os.remove(path=MEDIA_ROOT + '/' + str(self.logo_album))


class Musica(models.Model):
    nome_musica = models.CharField(max_length=40)
    album_musica = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    arquivo_musica = models.FileField(upload_to=user_directory_path_song)

    def __str__(self):
        return self.nome_musica + ' ' + str(self.album_musica)
    
    def delete_media(self):
        os.remove(path=MEDIA_ROOT + '/' + str(self.arquivo_musica))
from django.db import models
from datetime import date

# Create your models here.
class Actu(models.Model):

    titre = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    img = models.ImageField(upload_to="static/articles-pictures", blank=True, null=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.titre} - {self.date}"


class Album(models.Model):
    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True, null=True)
    couverture = models.ImageField(
        upload_to="albums-pictures/",
        default="tournament-pictures/logo.png",
    )

    def __str__(self):
        return self.titre


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    titre = models.CharField(max_length=30, blank=True, null=True)
    img = models.ImageField(
        upload_to="tournament-pictures/",
        default="profile-pictures/U9-mixte.png",
    )

    def __str__(self):
        return self.titre

from django.db import models
from datetime import date

# Create your models here.


class Section(models.Model):
    nom = models.CharField(max_length=30)
    img = models.ImageField(
        upload_to="tournament-pictures/",
        default="profile-pictures/U9-mixte.png",
    )
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nom}"


class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(
        upload_to="tournament-pictures/",
        default="profile-pictures/U9-mixte.png",
    )

    def __str__(self):
        return f"{self.nom}"


class Joueur(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.prenom} {self.nom} | Equipe : {self.equipe}"


class Event(models.Model):
    debut = models.TimeField(blank=True, null=True)
    fin = models.TimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Tournoi(models.Model):
    nom = models.CharField(max_length=30)
    lieu = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom


class Match(Event):
    tournoi = models.ForeignKey(Tournoi, on_delete=models.PROTECT, null=True)
    division = models.CharField(max_length=20)
    date = models.DateField()
    equipe_1 = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    equipe_2 = models.CharField(max_length=100)
    score_1 = models.IntegerField(default=0)
    score_2 = models.IntegerField(default=0)
    forfait_1 = models.BooleanField(default=False)
    forfait_2 = models.BooleanField(default=False)
    a_venir = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.equipe_1} VS {self.equipe_2} | {self.date}"

    def save(self, *args, **kwargs):
        if self.date < date.today():
            self.a_venir = False

        if self.score_1 or self.score_2:
            self.a_venir = False

        super(Match, self).save(*args, **kwargs)


class Entrainement(Event):
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=True, null=True)

    LU = "LU", "Lundi"
    MA = "MA", "Mardi"
    ME = "ME", "Mercredi"
    JE = "JE", "Jeudi"
    VE = "VE", "Vendredi"
    SA = "SA", "Samedi"
    JOURS = [LU, MA, ME, JE, VE, SA]
    jour = models.CharField(max_length=10, choices=JOURS)

    SP = "SP", "Salle polyvalente"
    G = "G", "Gymnase"
    HS = "H", "Halle des sports"
    LL = "LL", "Lycée Lafayette"
    SALLES = [SP, G, HS, LL]
    salle = models.CharField(max_length=10, choices=SALLES, default="SP")

    HEB = "HEB", "Hebdomadaire"
    MEN = "MEN", "Mensuel"
    UNE = "UNE", "Une fois"
    FREQUENCES = [HEB, MEN, UNE]
    frequence = models.CharField(max_length=5, choices=FREQUENCES, default="UNE")

    def __str__(self):
        salle = self.get_salle_display()
        jour = self.get_jour_display()
        frequence = self.get_frequence_display()

        return f"{self.equipe} | {salle} | {jour} | {frequence}"

from django.db import models
from django.forms import CharField, EmailField
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
from bbb.settings import SENDGRID_API_KEY
from rest_framework.exceptions import APIException

# Create your models here.
class Profil(models.Model):

    FUNC = "FUNC", "Equipe Fonctionnelle"
    TECH = "TECH", "Equipe Technique"
    COM = "COM", "Equipe de Communication"
    POLES = [FUNC, TECH, COM]
    pole = models.CharField(max_length=5, choices=POLES)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(
        upload_to="profile-pictures/",
        default="profile-pictures/profile-base.png",
    )

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.role}"


class Capacite(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)
    capacite = models.CharField(max_length=45)

    def save(self, *args, **kwargs):
        profil_capacites = Capacite.objects.filter(profil=self.profil)
        if len(profil_capacites) >= 2:
            raise APIException(
                detail="Un profil ne peut posséder que 2 capacités maximum", code=405
            )
        super(Capacite, self).save(*args, **kwargs)

    def __str__(self):
        return self.capacite


class Partenaire(models.Model):
    nom = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    img = models.ImageField(
        upload_to="partenaires-pictures/",
        default="profile-pictures/profile-base.png",
    )

    def __str__(self):
        return self.nom


class Licence(models.Model):
    prix = models.IntegerField()
    categorie = models.CharField(max_length=50)


class ContactForm(models.Model):
    expediteur = models.EmailField(max_length=254)
    prenom = models.CharField(max_length=30, blank=True, null=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    titre = models.CharField(max_length=30)
    message = models.CharField(max_length=5000)
    candidature = models.BooleanField(default=False)

    CREA = "CREA", "Création"
    REN = "REN", "Renouvellement"
    MUT = "MUT", "Mutation"
    LICENCES = [CREA, REN, MUT]
    licence = models.CharField(max_length=5, choices=LICENCES, blank=True, null=True)

    J = "J", "Joueur"
    E = "E", "Entraineur"
    B = "B", "Bénévole"
    STATUS = [J, E, B]
    status = models.CharField(max_length=1, choices=STATUS, blank=True, null=True)

    def __str__(self):
        return f"{self.expediteur} | {self.titre}"

    def save(self, *args, **kwargs):

        licence = self.get_licence_display()
        status = self.get_status_display()

        if self.candidature == True:
            message = Mail(
                from_email="bbb.contact.basket@gmail.com",
                to_emails=[To("marine.deletangbap@gmail.com"), To("aurebes@gmail.com")],
                subject=self.titre,
                html_content=f"<strong>Candidature de</strong> : {self.prenom} {self.nom} <br>"
                + f"<strong>Tel</strong> : {self.telephone} <br>"
                + f"<strong>Email</strong> : {self.expediteur}"
                + "<br><br>"
                + "<strong>Objet</strong> : Candidature en tant que "
                + status
                + "<br>"
                + "<strong>Type de la licence</strong> : "
                + licence
                + "<br><br>"
                + self.message,
            )
        else:
            message = Mail(
                from_email="bbb.contact.basket@gmail.com",
                to_emails=[To("marine.deletangbap@gmail.com"), To("aurebes@gmail.com")],
                subject=self.titre,
                html_content="<strong>Demande de contact de la part de : </strong>"
                + self.expediteur
                + "<br>"
                + "<strong>Objet : </strong>"
                + self.titre
                + "<br><br>"
                + self.message,
            )
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print("Exeception:", e)
        super(ContactForm, self).save(*args, **kwargs)

# Generated by Django 4.1.4 on 2022-12-07 15:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resultat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score_nous", models.IntegerField()),
                ("score_eux", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Tournoi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categorie", models.CharField(max_length=5)),
                ("date", models.DateField(default=datetime.date.today)),
                ("debut", models.TimeField(default=django.utils.timezone.now)),
                ("fin", models.TimeField(blank=True, null=True)),
                ("advers", models.CharField(max_length=100)),
                ("lieu", models.CharField(max_length=100)),
                (
                    "resultat",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="basket.resultat",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="basket.section",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=30)),
                (
                    "img",
                    models.ImageField(
                        default="profile-pictures/U9-mixte.png",
                        upload_to="tounament-pictures/",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="basket.section",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Entrainement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categorie", models.CharField(max_length=5)),
                ("date", models.DateField(default=datetime.date.today)),
                ("debut", models.TimeField(default=django.utils.timezone.now)),
                ("fin", models.TimeField(blank=True, null=True)),
                ("jour", models.CharField(max_length=10)),
                (
                    "section",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="basket.section",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

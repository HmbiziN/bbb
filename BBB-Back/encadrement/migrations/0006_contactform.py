# Generated by Django 4.1.3 on 2022-12-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("encadrement", "0005_rename_team_profil_pole"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactForm",
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
            ],
        ),
    ]

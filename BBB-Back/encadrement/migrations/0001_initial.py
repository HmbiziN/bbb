# Generated by Django 4.1.3 on 2022-12-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "team",
                    models.CharField(
                        choices=[
                            ("FUNC", "Functional Team"),
                            ("TECH", "Technical Team"),
                            ("COM", "Communication Team"),
                        ],
                        max_length=5,
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("function", models.CharField(max_length=50)),
                ("img", models.ImageField(upload_to="files/profile-pictures")),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("basket", "0014_remove_match_forfait_1_remove_match_forfait_2_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resultat",
            name="tournoi",
        ),
        migrations.AddField(
            model_name="resultat",
            name="match",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="basket.match",
            ),
        ),
    ]

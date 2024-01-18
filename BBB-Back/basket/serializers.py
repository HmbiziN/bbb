from rest_framework import serializers
import json
from basket.models import (
    Match,
    Tournoi,
    Entrainement,
    Section,
    Equipe,
    Joueur,
)


class MatchSerializer(serializers.ModelSerializer):
    section = serializers.SerializerMethodField()
    equipe_1 = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = (
            "id",
            "section",
            "equipe_1",
            "equipe_2",
            "date",
            "debut",
            "fin",
            "score_1",
            "score_2",
            "forfait_1",
            "forfait_2",
            "a_venir",
        )
        read_only_fields = ("a_venir",)

    def get_section(self, instance):
        section = instance.equipe_1.section
        return section.id

    def get_equipe_1(self, instance):
        equipe_1 = Equipe.objects.get(id=instance.equipe_1.id)
        serializer = EquipeSerializer(equipe_1)
        return serializer.data


class TournoiSerializer(serializers.ModelSerializer):
    matchs = serializers.SerializerMethodField()

    class Meta:
        model = Tournoi
        fields = ("id", "nom", "matchs")

    def get_matchs(self, instance):
        try:
            matchs = Match.objects.filter(tournoi=instance)
            serializer = MatchSerializer(matchs, many=True)
            return serializer.data
        except:
            pass


class EntrainementSerializer(serializers.ModelSerializer):
    salle = serializers.SerializerMethodField()
    equipe = serializers.SerializerMethodField()

    class Meta:
        model = Entrainement
        fields = "__all__"

    def get_salle(self, instance):
        salle = instance.get_salle_display()
        return salle

    def get_equipe(self, instance):
        try:
            equipe = Equipe.objects.get(id=instance.equipe.id)
            serializer = EquipeSerializer(equipe)
            return serializer.data
        except:
            pass


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = "__all__"


class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueur
        fields = "__all__"

from basket.serializers import (
    MatchSerializer,
    EntrainementSerializer,
    TournoiSerializer,
    SectionSerializer,
    EquipeSerializer,
    JoueurSerializer,
)

from basket.models import (
    Match,
    Tournoi,
    Entrainement,
    Section,
    Equipe,
    Joueur,
)
from rest_framework.viewsets import ModelViewSet
import datetime


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all().order_by("-date")
    serializer_class = MatchSerializer

    # Manual Filter to be able to slice queryset and filter at the same time
    def get_queryset(self):

        queryset = self.queryset
        current_date = datetime.date.today()

        if self.request.GET.get("section"):
            section = self.request.GET.get("section")
            queryset = queryset.filter(equipe_1__section=section)

        if self.request.GET.get("section_nom"):
            section = self.request.GET.get("section_nom")
            queryset = queryset.filter(equipe_1__section__nom=section)

        if self.request.GET.get("a_venir"):
            a_venir = self.request.GET.get("a_venir")
            queryset = queryset.filter(a_venir=a_venir)

        if self.request.GET.get("mois"):
            mois = self.request.GET.get("mois")
            queryset = queryset.filter(date__month=mois)

        queryset = queryset.filter(
            date__range=[
                current_date - datetime.timedelta(90),
                current_date + datetime.timedelta(90),
            ]
        )
        return queryset


class TournoiViewSet(ModelViewSet):
    queryset = Tournoi.objects.all()
    serializer_class = TournoiSerializer


class EntrainementViewSet(ModelViewSet):
    queryset = Entrainement.objects.all()
    serializer_class = EntrainementSerializer

    filterset_fields = ["equipe", "jour", "frequence", "salle"]


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class EquipeViewSet(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

    filterset_fields = [
        "section",
    ]


class JoueurViewSet(ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer

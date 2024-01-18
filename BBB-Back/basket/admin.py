from django.contrib import admin

from basket.models import (
    Match,
    Tournoi,
    Entrainement,
    Section,
    Equipe,
    Joueur,
)


class TournoiAdmin(admin.ModelAdmin):
    list_display = ("nom", "lieu")
    list_display_links = ("nom", "lieu")
    ordering = ("nom",)
    search_fields = ("nom", "lieu")


class MatchAdmin(admin.ModelAdmin):
    def gagnant(self, obj):
        if obj.forfait_1:
            return obj.equipe_2
        elif obj.forfait_2:
            return obj.equipe_1
        if obj.score_1!=0 or obj.score_2!=0:
            if obj.score_1 > obj.score_2:
                return obj.equipe_1
        elif obj.score_1 == obj.score_2:
            return "Egalité"
        else:
            return obj.equipe_2
        if obj.score_1 > obj.score_2:
            return obj.equipe_1
        elif obj.score_1 == obj.score_2:
            return "Egalité"
        else:
            return obj.equipe_2

    list_display = (
        "tournoi",
        "division",
        "date",
        "equipe_1",
        "equipe_2",
        "score_1",
        "score_2",
        "a_venir",
        "gagnant",
    )
    list_display_links = (
        "tournoi",
        "division",
        "date",
        "equipe_1",
        "equipe_2",
        "a_venir",
    )
    ordering = ("-date",)
    search_fields = ("division", "date", "equipe_1__nom", "equipe_2", "a_venir")
    list_filter = ("tournoi", "division", "equipe_1__nom", "a_venir")
    readonly_fields = ["a_venir", "gagnant"]


class EntrainementAdmin(admin.ModelAdmin):
    list_display = ("equipe", "date", "jour", "salle", "frequence")
    list_display_links = ("equipe", "date", "jour", "salle", "frequence")
    ordering = ("jour",)
    search_fields = ("date", "equipe__nom", "jour", "salle", "frequence")
    list_filter = ("frequence", "jour", "salle", "equipe__nom")


class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "description",
        "img",
    )
    list_display_links = (
        "nom",
        "description",
        "img",
    )
    search_fields = ("nom", "description")


class EquipeAdmin(admin.ModelAdmin):
    list_display = ("nom", "section")
    list_display_links = (
        "nom",
        "section",
    )
    ordering = ("section__nom",)
    search_fields = ("nom", "section__nom")
    list_filter = ("section",)
class JoueurAdmin(admin.ModelAdmin):
    list_display = ("equipe", "prenom", "nom", "age")
    list_display_links = ("equipe", "prenom", "nom", "age")
    ordering = ("age",)
    search_fields = ("equipe", "prenom", "nom", "age")
    list_filter = ("equipe",)


admin.site.register(Match, MatchAdmin)
admin.site.register(Entrainement, EntrainementAdmin)
admin.site.register(Tournoi, TournoiAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Joueur, JoueurAdmin)

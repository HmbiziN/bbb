from django.contrib import admin

# Register your models here.
from django.contrib import admin
from encadrement.models import Partenaire, Profil, Capacite, Licence


class ProfilAdmin(admin.ModelAdmin):
    list_display = (
        "prenom",
        "nom",
        "role",
        "pole",
    )
    list_display_links = (
        "prenom",
        "nom",
        "role",
        "pole",
    )
    ordering = ("nom",)
    search_fields = ("pole", "prenom", "nom", "role")
    list_filter = (
        "pole",
        "role",
    )


class PartenaireAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    list_display_links = ("nom",)
    ordering = ("nom",)
    search_fields = ("nom",)


class CapaciteAdmin(admin.ModelAdmin):
    list_display = ("capacite", "profil")
    list_display_links = ("capacite",)
    ordering = ("profil",)
    search_fields = ("capacite", "profil")


class LicenceAdmin(admin.ModelAdmin):
    list_display = ("prix", "categorie")
    list_display_links = ("prix", "categorie")
    ordering = ("categorie",)
    search_fields = ("categorie",)


admin.site.register(Profil, ProfilAdmin)
admin.site.register(Capacite, CapaciteAdmin)
admin.site.register(Partenaire, PartenaireAdmin)
admin.site.register(Licence, LicenceAdmin)

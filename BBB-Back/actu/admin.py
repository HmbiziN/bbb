from django.contrib import admin
from actu.models import Actu, Album, Photo


class ActuAdmin(admin.ModelAdmin):
    list_display = ("titre", "date")
    list_display_links = ("titre", "date")
    ordering = ("-date",)
    search_fields = ("titre", "date", "content")


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("titre",)
    list_display_links = ("titre",)
    search_fields = ("titre",)


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "album",
        "titre",
    )
    list_display_links = (
        "album",
        "titre",
    )
    search_fields = ("album__titre", "titre")


admin.site.register(Actu, ActuAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)

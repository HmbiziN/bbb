"""bbb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from bbb import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from basket.views import (
    MatchViewSet,
    TournoiViewSet,
    EntrainementViewSet,
    SectionViewSet,
    EquipeViewSet,
    JoueurViewSet,
)

from encadrement.views import (
    ProfilViewSet,
    PartenaireViewSet,
    ContactFormViewSet,
    LicenceViewSet,
)
from actu.views import ActuViewSet, PhotoViewSet, AlbumViewSet

admin.site.site_header = "BBB Administrateurs"

router = routers.DefaultRouter()

router.register("match", MatchViewSet)
router.register("tournoi", TournoiViewSet)
router.register("entrainement", EntrainementViewSet)
router.register("section", SectionViewSet)
router.register("profil", ProfilViewSet)
router.register("licence", LicenceViewSet)
router.register("partenaire", PartenaireViewSet)
router.register("actu", ActuViewSet)
router.register("equipe", EquipeViewSet)
router.register("joueur", JoueurViewSet)
router.register("contact-form", ContactFormViewSet)
router.register("photo", PhotoViewSet)
router.register("album", AlbumViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# TODO interface admin

# TODO permissions
# permissions pour create/update/partial_update


# Super admin avec "ajouter un club"
# Administrateurs Club

# Toutes les tables sont un club

# Pour frontend en fonction de l'url, on ajoute un paramètre qui accède au backend, puis ajouter ce paramètre dans le backend

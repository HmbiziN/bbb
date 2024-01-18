from encadrement.models import Profil, Partenaire, ContactForm, Licence
from encadrement.serializers import (
    ProfilSerializer,
    PartenaireSerializer,
    ContactFormSerializer,
    LicenceSerializer,
)
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProfilViewSet(ModelViewSet):  # TODO: make filters work
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    filterset_fields = [
        "pole",
        "prenom",
        "nom",
    ]


class LicenceViewSet(ModelViewSet):
    queryset = Licence.objects.all()
    serializer_class = LicenceSerializer


class PartenaireViewSet(ModelViewSet):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer


class ContactFormViewSet(ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

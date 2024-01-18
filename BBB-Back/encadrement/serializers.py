from encadrement.models import Profil, Partenaire, ContactForm, Capacite, Licence
from rest_framework import serializers


class CapaciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacite
        fields = "__all__"


class ProfilSerializer(serializers.ModelSerializer):
    capacites = serializers.SerializerMethodField()

    class Meta:
        model = Profil
        fields = "__all__"
        optional_fields = [
            "img",
        ]

    def get_capacites(self, instance):
        capacites = Capacite.objects.filter(profil=instance)
        serializer = CapaciteSerializer(capacites, many=True)
        return serializer.data


class PartenaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenaire
        fields = "__all__"


class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        fields = "__all__"


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"

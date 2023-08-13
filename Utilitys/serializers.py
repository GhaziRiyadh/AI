from rest_framework import serializers

from Utilitys.models import Main

class MainSerializer(serializers.Serializer):
    class Meta:
        model = Main
        fields = '__all__'
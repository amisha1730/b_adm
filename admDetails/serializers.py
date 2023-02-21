from rest_framework import serializers
from .models import AdmDetail
# from doctor.serializers import admSerializer
from specializations.serializers import SpecializationSerializer


class CreateAdmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmDetail
        fields = '__all__'

class ListAdmDetailSerializer(serializers.ModelSerializer):
    # doctor = AdmSerializer(read_only=True)
    specialization= SpecializationSerializer(read_only=True,many=True)
    class Meta:
        model = AdmDetail
        fields = '__all__'



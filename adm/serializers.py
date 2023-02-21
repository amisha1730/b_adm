from rest_framework import serializers
from .models import Adm
from admDetails.serializers import ListAdmDetailSerializer


class AdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adm
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ListAdmSerializer(serializers.ModelSerializer):
    admdetail = ListAdmDetailSerializer(read_only=True)
    class Meta:
        model = Adm
        fields = ['id', 'name', 'email', 'password','admdetail']
        extra_kwargs = {
            'password': {'write_only': True}
        }



        

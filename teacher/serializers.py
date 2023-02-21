from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'subject']
      
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

# class ListAdmSerializer(serializers.ModelSerializer):
#     admdetail = ListAdmDetailSerializer(read_only=True)
#     class Meta:
#         model = Adm
#         fields = ['id', 'name', 'email', 'password','admdetail']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }



        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .serializers import AdmSerializer,ListAdmSerializer
from .models import Adm
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

# class RegisterView(APIView):
class RegisterView(APIView):
    def post(self, request):
        serializer = AdmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        adm=serializer.save()
        tokenr = TokenObtainPairSerializer().get_token(adm)  
        tokena = AccessToken().for_user(adm)
        tokena['email'] = adm.email
        tokena['role'] = adm.role
        response = Response()
        response.data = {
            'student':serializer.data,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response




class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        adm = Adm.objects.filter(email=email).first()
        if adm is None:
            raise AuthenticationFailed('adm not found!')
        if not adm.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        tokenr = TokenObtainPairSerializer().get_token(adm)  
        tokena = AccessToken().for_user(adm)
        tokena['email'] = adm.email
        tokena['role'] = adm.role
        response = Response()
        response.set_cookie(key='jwt', value=tokena, httponly=True)
        response.data = {
            'id':adm.id,
            'email':adm.email,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response


class getAdm(APIView):
    def get(self, request):
        adm = Adm.objects.select_related('admdetail').all()
        print("this is the detail".admdetail)
        serializer = AdmSerializer(adm,many=True)
        return Response(serializer.data)

class getAdmById(APIView):
    def get(self, request,id):
        adm = Adm.objects.select_related('admdetail').get(id=id)
        print("this is the detail".admdetail.id)
        serializer=ListAdmSerializer(adm,many=False)
        return Response(serializer.data)

class updateAdm(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,id):
        adm= Adm.objects.get(id=id)
        serializer=AdmSerializer(instance=adm,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteAdm(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request,id):
        adm= Adm.objects.get(id=id)
        adm.delete()
        return Response("Item Successfully Deleted")

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class ValidateToken(APIView):
    def get(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            data=jwt.decode(token, "secret", algorithms=["HS256"])
            return Response(data)
        except Exception as e:
            return Response(e)
        


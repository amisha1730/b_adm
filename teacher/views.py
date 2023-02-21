from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view

import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
import requests
import json

class AddTeacher(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        teacher = requests.post('http://localhost:8080/teacher/register',request.data)
        response=json.loads(teacher.text)
        return Response(response)
        
class UpdateTeacher(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        teacher = requests.patch(f'http://localhost:8080/teacher/update/{id}',request.data)
        response=json.loads(teacher.text)
        return Response(response)

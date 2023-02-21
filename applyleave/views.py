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
class ApproveLeave(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        student = requests.patch(f'http://localhost:8080/applyLeave/approve/{id}',{'status':request.data.status})
        response=json.loads(student.text)
        return Response(response)

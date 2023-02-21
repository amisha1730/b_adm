from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateAdmDetailSerializer,ListAdmDetailSerializer
from specializations.models import Specialization
from .models import AdmDetail
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createAdmDetail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        adm= request.user
        request.data['adm']= adm
        data=request.data
        newAdmDetail= AdmDetail.objects.create(contact=data['contact'],address=data['address'],additionalInfo=data['additionalInfo'],inTime=data['inTime'],outTime=data['outTime'],adm=data['adm'])
        for specializationId in data['specialization']:
            specialization=Specialization.objects.get(id=specializationId)
            newAdmDetail.specialization.add(specialization)
        serializer = CreateAdmDetailSerializer(newAdmDetail) 
        return Response(serializer.data)

class getAdmDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data=request.data
        admDetails = AdmDetail.objects.all()
        serializer=ListAdmDetailSerializer(admDetails,many=True)
        return Response(serializer.data)

class getAdmDetailById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        admDetail = AdmDetail.objects.get(id=id)
        serializer=ListAdmDetailSerializer(admDetail,many=False)
        return Response(serializer.data)

class updateAdmDetail(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        data=request.data
        admDetail = AdmDetail.objects.get(id=id)
        admDetail.specialization.clear() 
        for specializationId in data['specialization']:
            specialization=Specialization.objects.get(id=specializationId)
            admDetail.specialization.add(specialization)
        serializer=CreateAdmDetailSerializer(instance=admDetail,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteAdmDetail(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        admDetail = AdmDetail.objects.get(id=id)
        print("this is the AdmDetail",admDetail)
        admDetail.delete()
        return Response("Item Successfully Deleted")



    
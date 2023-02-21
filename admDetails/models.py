from django.db import models
from adm.models import Adm
from specializations.models import Specialization

class AdmDetail(models.Model):
    id=models.AutoField(primary_key=True)
    contact= models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    additionalInfo= models.CharField(max_length=255)
    specialization=models.ManyToManyField(Specialization)
    inTime=models.TimeField()
    outTime=models.TimeField()
    adm = models.OneToOneField(
        Adm,
        on_delete=models.CASCADE,
    )
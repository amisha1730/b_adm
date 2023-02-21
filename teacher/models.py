from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum



class Teacher(models.Model):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255,unique=True)
    subject= models.CharField(max_length=255)
    REQUIRED_FIELDS=[]

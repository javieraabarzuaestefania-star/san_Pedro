from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROL_CHOICES= [
        ('paciente','Paciente'),
        ('recepcionista','Recepcionista'),
        ('medico','Medico'),
    ]

    rut = models.CharField(max_length=12,unique=True)
    rol=  models.CharField(max_length=20,choices= ROL_CHOICES)

    email = models.EmailField(unique=True)
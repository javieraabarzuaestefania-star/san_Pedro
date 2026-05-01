from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, rut, password=None, **extra_fields):
        if not rut:
            raise ValueError('El Rut es obligatorio')
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,rut,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
  
        return self.create_user(rut, password, **extra_fields)

class User(AbstractUser):
    username=None
    ROL_CHOICES= [
        ('paciente','Paciente'),
        ('recepcionista','Recepcionista'),
        ('medico','Medico'),
    ]

    rut = models.CharField(max_length=12,unique=True)
    rol=  models.CharField(max_length=20,choices= ROL_CHOICES,null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = []


    
    objects = UserManager()


    def __str__(self):
        return self.rut


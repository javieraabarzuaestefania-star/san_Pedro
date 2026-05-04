from django.urls import path
from .views import *
from .views import agenda_medico

urlpatterns = [
    path('crear/', crear_horario, name='crear_horario'),
    path('ver/', agenda_medico, name='agenda_medico'),
]
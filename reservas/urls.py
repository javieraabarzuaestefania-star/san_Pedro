from django.urls import path
from .views import *
from .views import cancelar_reserva, reprogramar_reserva

urlpatterns = [
    path('horas/', ver_horas, name='ver_horas'),
    path('reservar/<int:id>/', reservar_hora, name='reservar_hora'),
    path('cancelar/<int:id>/', cancelar_reserva, name='cancelar_reserva'),
    path('mis/', mis_reservas, name='mis_reservas'),
    path('reprogramar/<int:id>/', reprogramar_reserva, name='reprogramar_reserva'),
]
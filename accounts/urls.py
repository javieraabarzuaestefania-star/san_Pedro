from django.urls import path
from .views import * 

urlpatterns = [
    path('', login_view, name='login'),
    path('paciente/', panel_paciente, name='panel_paciente'),
    path('medico/', panel_medico, name='panel_medico'),
    path('recepcion/', panel_recepcionista, name='panel_recepcionista'),
    path('logout/', logout_view, name= 'logout'),
    path('registro/',registro_view, name='registro'),
    path('buscar/', buscar_paciente, name='buscar_paciente'),
    path('reservas-paciente/', ver_reservas_paciente, name='ver_reservas_paciente'),
]
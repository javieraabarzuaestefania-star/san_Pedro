from django.db import models
from accounts.models import User
from agenda.models import HorarioDisponible

class Reserva(models.Model):
    paciente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'rol': 'paciente'}
    )
    horario = models.OneToOneField(HorarioDisponible, on_delete=models.CASCADE)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente.rut} - {self.horario}"

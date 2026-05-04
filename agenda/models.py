from django.db import models
from accounts.models import User

class HorarioDisponible(models.Model):
    medico = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'rol': 'medico'}
    )
    fecha = models.DateField()
    hora = models.TimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.medico.rut} - {self.fecha} {self.hora}"
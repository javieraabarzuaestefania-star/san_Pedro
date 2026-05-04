from django.shortcuts import render, redirect
from .models import HorarioDisponible
from reservas.models import Reserva
from accounts.models import User

horas = HorarioDisponible.objects.filter(
    disponible=True,
    medico__rol='medico'
)

def crear_horario(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        hora = request.POST['hora']

        HorarioDisponible.objects.create(
            medico=request.user,
            fecha=fecha,
            hora=hora
        )
        return redirect('panel_medico')

    return render(request, 'agenda/crear_horario.html')

def agenda_medico(request):
    return render(request, 'agenda/agenda_medico.html')


def agenda_medico(request):
    reservas = Reserva.objects.filter(horario__medico=request.user)
    return render(request, 'agenda/agenda_medico.html', {'reservas': reservas})



def reservar_por_rut(request, id):
    if request.method == 'POST':
        rut = request.POST['rut']
        paciente = User.objects.get(rut=rut)

        horario = HorarioDisponible.objects.get(id=id)

        Reserva.objects.create(
            paciente=paciente,
            horario=horario
        )

        horario.disponible = False
        horario.save()

        return redirect('panel_recepcionista')

def mis_reservas(request):
    reservas = Reserva.objects.filter(paciente=request.user)
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})
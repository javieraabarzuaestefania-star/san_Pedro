from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from agenda.models import HorarioDisponible
from .models import Reserva

def ver_horas(request):
    horas = HorarioDisponible.objects.filter(disponible=True)
    return render(request, 'reservas/ver_horas.html', {'horas': horas})
def reservar_hora(request, id):
    horario = get_object_or_404(HorarioDisponible, id=id)

    Reserva.objects.create(
        paciente=request.user,
        horario=horario
    )

    horario.disponible = False
    horario.save()

    return redirect('panel_paciente')
def cancelar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.horario.disponible = True
    reserva.horario.save()
    reserva.delete()

    return redirect('panel_paciente')
def agenda_medico(request):
    reservas = Reserva.objects.filter(horario__medico=request.user)
    return render(request, 'agenda/agenda_medico.html', {'reservas': reservas})

def mis_reservas(request):
    reservas = Reserva.objects.filter(paciente=request.user)
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})

def reprogramar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)

    # liberar horario antiguo
    reserva.horario.disponible = True
    reserva.horario.save()

    reserva.delete()

    return redirect('ver_horas')

def reservar_hora(request, id):
    horario = get_object_or_404(HorarioDisponible, id=id)

    Reserva.objects.create(
        paciente=request.user,
        horario=horario
    )

    horario.disponible = False
    horario.save()

    return redirect('mis_reservas')
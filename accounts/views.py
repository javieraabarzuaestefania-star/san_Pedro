from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import User
from reservas.models import Reserva


# =========================
# REGISTRO
# =========================
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {'form': form})


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
# LOGIN
# =========================
def login_view(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        password = request.POST['password']

        user = authenticate(request, rut=rut, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')

            elif user.rol == 'paciente':
                return redirect('panel_paciente')

            elif user.rol == 'medico':
                return redirect('panel_medico')

            elif user.rol == 'recepcionista':
                return redirect('panel_recepcionista')

    return render(request, 'accounts/login.html')


# =========================
# PANELES
# =========================
@login_required
def panel_paciente(request):
    return render(request, 'accounts/paciente.html')


@login_required
def panel_medico(request):
    return render(request, 'accounts/medico.html')


@login_required
def panel_recepcionista(request):
    return render(request, 'accounts/recepcionista.html')


# =========================
# 🔍 BUSCAR PACIENTE (NUEVO)
# =========================
@login_required
def buscar_paciente(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')

        try:
            paciente = User.objects.get(rut=rut, rol='paciente')

            # guardamos en sesión
            request.session['paciente_id'] = paciente.id

            return redirect('ver_reservas_paciente')

        except User.DoesNotExist:
            return render(request, 'accounts/buscar_paciente.html', {
                'error': 'Paciente no encontrado'
            })

    return render(request, 'accounts/buscar_paciente.html')


# =========================
# 📋 VER RESERVAS DEL PACIENTE (NUEVO)
# =========================
@login_required
def ver_reservas_paciente(request):
    paciente_id = request.session.get('paciente_id')

    reservas = Reserva.objects.filter(paciente_id=paciente_id)

    return render(request, 'accounts/reservas_paciente.html', {
        'reservas': reservas
    })
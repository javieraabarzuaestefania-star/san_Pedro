from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm


# REGISTRO
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


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# LOGIN
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


# PANELES
@login_required
def panel_paciente(request):
    return render(request, 'accounts/paciente.html')


@login_required
def panel_medico(request):
    return render(request, 'accounts/medico.html')


@login_required
def panel_recepcionista(request):
    return render(request, 'accounts/recepcionista.html')
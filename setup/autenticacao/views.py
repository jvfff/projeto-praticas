from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from .forms import ONGProfileForm, VolunteerProfileForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_type = form.cleaned_data.get('user_type')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user_type == 'ONG':
                return redirect('registro_ong')
            else:
                return redirect('registro_voluntario')
    else:
        form = RegistroForm()
    return render(request, 'autenticacao/registro.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'autenticacao/login.html', {'form': form})

@login_required
def index(request):
    return render(request, 'autenticacao/index.html')

@login_required
def registro_ong(request):
    if request.method == 'POST':
        form = ONGProfileForm(request.POST)
        if form.is_valid():
            ong_profile = form.save(commit=False)
            ong_profile.user = request.user
            ong_profile.save()
            return redirect('index') 
    else:
        form = ONGProfileForm()
    return render(request, 'autenticacao/registro_ong.html', {'form': form})

@login_required
def registro_voluntario(request):
    if request.method == 'POST':
        form = VolunteerProfileForm(request.POST)
        if form.is_valid():
            volunteer_profile = form.save(commit=False)
            volunteer_profile.user = request.user
            volunteer_profile.save()
            return redirect('index')  
    else:
        form = VolunteerProfileForm()
    return render(request, 'autenticacao/registro_voluntario.html', {'form': form})


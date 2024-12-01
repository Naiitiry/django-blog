from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_user(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'El nombre de usuario ya está en uso.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'El correo ya registrado.')
            return redirect('register')
        
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        messages.success(request,'Usuario registrado con éxito.')
    return render(request,'accounts/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return  redirect('index')
        else:
            messages.error(request,'Credenciales inválidas.')
            return redirect('login')
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito.')
    return redirect('login')


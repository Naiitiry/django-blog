from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def register_user(request):
    if request.method=='GET':
        form=RegisterForm()
        context={
            'form':form
        }
        return render(request,'accounts/register.html',context)
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario registrado con éxito.')
            return redirect('index')#redirige a la página principal/index.
        """
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
        """
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Credenciales válidas.')
            return  redirect('post_index')
        else:
            messages.error(request,'Credenciales inválidas.')
            return redirect('login')
    return render(request,'accounts/login.html',{})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito.')
    return redirect('login')


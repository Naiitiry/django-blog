from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
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
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return  redirect('index')


@login_required
def index(request):
    return render(request,'post/index.html',{})

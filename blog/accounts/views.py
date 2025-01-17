from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm

#################################################################################
#                    LOGIN - REGISTER - LOGOUT                                  #
#################################################################################

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
            return redirect('login')#redirige a la página principal/index.
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    if request.method == 'GET':
        form_log=LoginForm()
        context={
            'form_log':form_log
        }
        return render(request,'accounts/login.html',context)
    elif request.method == 'POST':
        form_log=LoginForm(request.POST)
        if form_log.is_valid():
            username=form_log.cleaned_data['username']
            password=form_log.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'Bienvenido {username}')
                return redirect('post_index')
            else:
                messages.error(request,'Credenciales inválidas.')
        else:
            messages.error(request,'Datos erroneos, ingresa usuario y/o contraseña correctamente.')
        context = {
                'form_log': form_log
            }
        return render(request,'accounts/login.html',context)
    elif request.user.is_authenticated:
        return redirect('post_index')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito.')
    return redirect('login')

#################################################################################
#                                   USUARIOS                                    #
#################################################################################

@login_required
def user_detail(request,user_id=None):
    if user_id:
        user_profile = get_object_or_404(User,id=user_id)
    else:
        user_profile=request.user
    
    is_owner = request.user == user_profile
    is_admin = request.user.groups.filter(name='Admin').exists()

    user_posts = user_profile.posts.filter(is_deleted=False)
    context={
        'user_profile':user_profile,
        'user_post':user_posts,
        'is_owner':is_owner,
        'is_admin':is_admin,
    }
    return render(request,'accounts/detail.html',context)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        return redirect('post_index')
    else:
        return render(request,'index.html')

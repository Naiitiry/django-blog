from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


@login_required
def index(request):
    posts=Post.objects.filter(is_deleted=False,title__contains=request.GET.get('search',''))
    context={
        'posts':posts
    }
    return render(request,'post/post_index.html',context)

@login_required
def view(request,id):
    post=Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request,'post/detail.html',context)

@login_required
def edit(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'GET':
        form=PostForm(instance=post)
        context={
            'form':form,
            'id':id
        }
        return render(request,'post/edit.html',context)
    if request.method == 'POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        context={
            'form':form,
            'id':id
        }
        messages.success(request,'Post actualizado con éxito.')
        return render(request,'post/edit.html',context)
    
@login_required
def create(request):
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('post_index')
        else:
            context={
                'form':form
            }
            return render(request,'post/create.html',context)
    else:
        form=PostForm()
        context={
                'form':form
            }
        return render(request,'post/create.html',context)
    
def delete(request,id):
    post=Post.objects.get(id=id,user=request.user)
    if post:
        post.is_deleted=True
        post.save()
        messages.success(request,'Post eliminado con éxito.')
    else:
        messages.error(request,'El post solicitado no existe.')
    return redirect('post_index')
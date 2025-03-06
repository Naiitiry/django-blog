from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Post, Comment
from .forms import PostForm, CommentForm


@login_required
def index(request):
    search_query = request.GET.get('search', '')
    posts = (Post.objects.filter(is_deleted=False, title__contains=search_query)
            .annotate(comment_count=Count('comments'))
            )
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj':page_obj,
        'search_query':search_query
    }
    return render(request,'post/post_index.html',context)

@login_required
def view(request,id):
    post=Post.objects.get(id=id)
    comments=post.comments.filter(is_deleted=False)
    context={
        'post':post,
        'comments':comments,
    }
    return render(request,'post/detail.html',context)

@login_required
def edit(request,id):
    post=get_object_or_404(Post,id=id)

    if request.user != post.user:
        messages.error(request,'No tienes los permisos para modificar el post.')
        return redirect('post_view',id=post.id)

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
            messages.success(request,"Post creado con éxito!")
            return redirect('post_index')
        else:
            context={
                'form':form
            }
            messages.error(request,"Error al crear el post.")
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

###################################################################
#                           COMMENTS                              #
###################################################################

@login_required
def add_comment(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment.objects.create(
                comment=comment_text,
                post=post,
                user=request.user,
            )
    return redirect('post_view',id=post.id)

@login_required
def edit_comment(request,id):
    comment = get_object_or_404(Comment, id=id)

    if request.user != comment.user:
        return redirect('post_view',id=comment.post.id)
    
    if request.method == 'POST':
        next_text = request.POST.get('comment')
        if next_text:
            comment.comment = next_text
            comment.save()
    context = {
        'post': comment.post,
        'comment': comment
    }
    return redirect('post_view',id=comment.post.id)

@login_required
def delete_comment(request,id):
    comment = get_object_or_404(Comment,id=id)
    if request.user == comment.user or request.user.is_staff:
        comment.is_deleted=True
        comment.save()
        messages.success(request,'Comentario eliminado con éxito!')
    else:
        messages.error(request,'No se pudo eliminar el comentario.')
    return redirect('post_view',id=comment.post.id)

###################################################################
#                            LIKES                                #
###################################################################


@login_required
def post_like(request,id):
    post = get_object_or_404(Post,id=id)
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_index')
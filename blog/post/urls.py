from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',views.index,name='post_index'),
    path('view/<int:id>/',views.view,name='post_view'),
    path('edit/<int:id>',views.edit,name='post_edit'),
    path('delete/<int:id>',views.delete,name='post_delete'),
    path('create/',views.create,name='post_create'),
    path('view/<int:id>/add_comment/',views.add_comment,name='add_comment'),
    path('edit_comment/<int:id>/',views.edit_comment,name='edit_comment'),
    path('delete_coment/<int:id>/',views.delete_comment,name='delete_comment'),
    path('post_like/<int:id>',views.post_like,name='post_like'),
    path('post_like_inpost/<int:id>',views.post_like_inpost,name='post_like_inpost')
]
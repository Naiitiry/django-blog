from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='post_index'),
    path('view/<int:id>',views.view,name='post_view'),
    path('edit/<int:id>',views.edit,name='post_edit'),
    path('delete/<int:id>',views.delete,name='post_delete'),
    path('create/',views.create,name='post_create'),
]
from . import views
from django.urls import path, include

urlpatterns = [
    path('login/',views.login_user,name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_view,name='logout'),
]
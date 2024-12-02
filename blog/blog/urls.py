from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='blog_index'),
    path('post/',include('post.urls')),
    path('accounts/',include('accounts.urls')),
    path('login/',RedirectView.as_view(url='/accounts/login/')),
]

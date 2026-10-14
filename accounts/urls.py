from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =  [
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ver_perfil', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil')
    ]

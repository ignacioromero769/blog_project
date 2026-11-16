from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =  [
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html', success_url='password_cambiada'), name='password_change'),
    path('password_change/password_cambiada/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_cambiada.html'), name='password_change_done')
    ]

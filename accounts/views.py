from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, PerfilForm
from .models import Perfil
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            return redirect("login")
    else:
        form = RegistroUsuarioForm()
        contexto = {"form":form}
        return render(request, "accounts/registro.html", contexto)

@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            form.save()
            return redirect("lista_posts")
    else:
        form = PerfilForm(instance=perfil)
        contexto = {"form":form}

        return render(request, "accounts/editar_perfil.html", contexto)

@login_required
def ver_perfil(request):
    user = request.user

    contexto = {"user":user}
    return render(request, "accounts/ver_perfil.html", contexto)





    

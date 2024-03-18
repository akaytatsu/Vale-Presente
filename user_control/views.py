from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms.add_user_forms import AddUserForm
from .models import UserActivities

def add_user_activity(user, action):
  UserActivities.objects.create(
    user_id=user.id,
    email=user.email,
    fullname=user.fullname,
    action=action
  )


@login_required
def cadastrar_usuario(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  if request.method == "POST":
    form_usuario = AddUserForm(request.POST)
    form_usuario.fields['fullname'].label = "Nome"
    if form_usuario.is_valid():
      form_usuario.save()
      return redirect('listar_usuarios')
  else:
    form_usuario = AddUserForm()
  return render(request, 'users/form_users.html', {'form_usuario': form_usuario})


@login_required
def listar_usuarios(request):
  User = get_user_model()
  usuarios = User.objects.all()
  return render(request, 'users/list_users.html', {'usuarios': usuarios})


@login_required
def deletar_usuario(request, id):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")

  User = get_user_model()
  usuario = get_object_or_404(User, id=id)

  if usuario.is_superuser:
    if not request.user.is_superuser:
      return HttpResponseForbidden("Acesso negado. Não é possível deletar um superusuário.")

  usuario.delete()
  return redirect('listar_usuarios')


@login_required
def editar_usuario(request, id):
  if not request.user.is_staff:
        return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  User = get_user_model()
  usuario = User.objects.get(id=id)
  form_usuario = AddUserForm(request.POST or None, instance=usuario)
  form_usuario.fields['fullname'].label = "Nome"

  if form_usuario.is_valid():
    form_usuario.save()
    return redirect('listar_usuarios')
  return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})


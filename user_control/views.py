from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
  return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})


from django.shortcuts import get_object_or_404, render, redirect
from user_control.models import CustomUser
from .forms.app_forms import AtualizarStatusRotinaForm, RotinaForm, DescricaoRelatorioForm
from .models import Rotina, Descricao_relatorio, Setor, StatusDiarioRotina
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def add_store(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  if request.method == 'POST':
    form = RotinaForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_rotina')
  else:
      form = RotinaForm()

  return render(request, 'app/add_store.html', {'form': form})


def edit_store(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
    rotina = Rotina.objects.get(id=id)
    if request.method == 'POST':
        form = RotinaForm(request.POST, instance=rotina)
        if form.is_valid():
            form.save()
            return redirect('listar_rotina')
    else:
        form = RotinaForm(instance=rotina)

    return render(request, 'app/add_or_edit_rotina.html', {'form': form})

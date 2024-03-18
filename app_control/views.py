from django.shortcuts import get_object_or_404, render, redirect
from user_control.models import CustomUser
from .forms.app_forms import AddGiftVoucherForm, AddStoreForm
from .models import Store, GiftVoucher
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def add_store(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  if request.method == 'POST':
    form = AddStoreForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('list_store')
  else:
      form = AddStoreForm()

  return render(request, 'app/add_store.html', {'form': form})


@login_required
def edit_store(request, id):
  if not request.user.is_staff:
      return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  rotina = Store.objects.get(id=id)
  if request.method == 'POST':
      form = AddStoreForm(request.POST, instance=rotina)
      if form.is_valid():
          form.save()
          return redirect('list_store')
  else:
      form = AddStoreForm(instance=rotina)

  return render(request, 'app/add_store.html', {'form': form})


@login_required
def delete_store(request, id):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  store = get_object_or_404(Store, id=id)
  store.delete()
  return redirect('list_store')


@login_required
def list_store(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  stores = Store.objects.all()
  return render(request, 'app/list_store.html', {'stores': stores})


def add_giftvoucher(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
    
    if request.method == 'POST':
        form = AddGiftVoucherForm(request.POST)
        if form.is_valid():
            gift_voucher = form.save()
            # Armazena o ID do source_store na sessão
            request.session['source_store_id'] = gift_voucher.source_store.id
            request.session['discount_price'] = str(gift_voucher.discount_price)
            return redirect('add_giftvoucher')
    else:
        initial_data = {}
        source_store_id = request.session.get('source_store_id')
        discount_price = request.session.get('discount_price')
        
        if source_store_id:
            initial_data['source_store'] = source_store_id
        if discount_price:
            initial_data['discount_price'] = discount_price
        
        form = AddGiftVoucherForm(initial=initial_data)

    return render(request, 'app/add_giftvoucher.html', {'form': form})


@login_required
def edit_giftvoucher(request, id):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  giftvoucher = GiftVoucher.objects.get(id=id)
  if request.method == 'POST':
    form = AddGiftVoucherForm(request.POST, instance=giftvoucher)
    if form.is_valid():
        form.save()
        return redirect('list_giftvoucher')
  else:
    form = AddStoreForm(instance=giftvoucher)

  return render(request, 'app/list_giftvoucher.html', {'form': form})


@login_required
def delete_giftvoucher(request, id):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  giftvoucher = get_object_or_404(GiftVoucher, id=id)
  giftvoucher.delete()
  return redirect('list_giftvoucher')


@login_required
def list_giftvoucher(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  giftvouchers = GiftVoucher.objects.all()
  return render(request, 'app/list_giftvoucher.html', {'giftvouchers': giftvouchers})


@login_required
def add_barcode(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")

  gift_voucher_id = request.session.get('gift_voucher_id', None)

  if request.method == 'POST':
    form = AddGiftVoucherForm(request.POST)
    if form.is_valid():
      bar_code = form.save(commit=False)
      if gift_voucher_id is not None:
          # Se já temos um gift voucher na sessão, use-o
          bar_code.GiftVoucher = get_object_or_404(GiftVoucher, id=gift_voucher_id)
      bar_code.save()
      # Atualiza o gift voucher na sessão
      request.session['gift_voucher_id'] = bar_code.GiftVoucher.id
      return redirect('add_barcode')  # Redireciona para a mesma página para adicionar outro código
  else:
    # Predefine o gift voucher no formulário se ele estiver na sessão
    form = AddGiftVoucherForm(initial={'GiftVoucher': gift_voucher_id} if gift_voucher_id else {})

  return render(request, 'app/add_barcode.html', {'form': form})


@login_required
def add_barcode(request):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")

  gift_voucher_id = request.session.get('gift_voucher_id', None)

  if request.method == 'POST':
    form = AddBarCodeForm(request.POST)
    if form.is_valid():
      bar_code = form.save(commit=False)
      if gift_voucher_id is not None:
          # Se já temos um gift voucher na sessão, use-o
          bar_code.GiftVoucher = get_object_or_404(GiftVoucher, id=gift_voucher_id)
      bar_code.save()
      # Atualiza o gift voucher na sessão
      request.session['gift_voucher_id'] = bar_code.GiftVoucher.id
      return redirect('add_barcode')  # Redireciona para a mesma página para adicionar outro código
  else:
    # Predefine o gift voucher no formulário se ele estiver na sessão
    form = AddBarCodeForm(initial={'GiftVoucher': gift_voucher_id} if gift_voucher_id else {})

  return render(request, 'app/add_barcode.html', {'form': form})


@login_required
def edit_barcode(request, id):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  giftvoucher = BarCode.objects.get(id=id)
  if request.method == 'POST':
    form = AddBarCodeForm(request.POST, instance=giftvoucher)
    if form.is_valid():
        form.save()
        return redirect('list_giftvoucher')
  else:
    form = AddBarCodeForm(instance=giftvoucher)

  return render(request, 'app/list_giftvoucher.html', {'form': form})


@login_required
def delete_barcode(request, id):
  if not request.user.is_staff:
    return HttpResponseForbidden("Acesso negado. Você precisa ser administrador.")
  barcode = get_object_or_404(BarCode, id=id)
  barcode.delete()
  return redirect('list_barcode')


@login_required
def list_barcode(request):
  giftvouchers = GiftVoucher.objects.all()
  query = request.GET.get('query', '')
  if query:
    giftvouchers = GiftVoucher.objects.filter(bar_code__icontains=query)
  return render(request, 'app/dashboard_barcode.html', {'giftvouchers': giftvouchers})


@login_required
def dashboard_barcode(request):
  bar_code = GiftVoucher.objects.all()
  return render(request, 'app/dashboard_barcode.html', {'bar_code': bar_code})


@login_required
def activities_barcode(request):
  bar_code = GiftVoucher.objects.filter(status_bar_code=False)
  return render(request, 'app/activities_barcode.html', {'bar_code': bar_code})


@login_required
def use_barcode(request, id):
  barcode = get_object_or_404(GiftVoucher, id=id)
  
  if hasattr(request.user, 'user_store') and request.user.user_store:
    barcode.store_used = request.user.user_store
    barcode.status_bar_code = True
    barcode.save()  # Salva as alterações no BarCode
    return redirect('list_barcode')  # Substitua 'list_barcode' pela URL de destino desejada
  else:
    # Caso o usuário não esteja associado a nenhuma loja
    return HttpResponseForbidden("Usuário não está associado a nenhuma loja.")
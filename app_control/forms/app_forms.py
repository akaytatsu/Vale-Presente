from django import forms
from user_control.models import CustomUser
from ..models import Store, GiftVoucher
from django.forms import ModelChoiceField
from django.utils import timezone


class AddStoreForm(forms.ModelForm):
  class Meta:
    model = Store
    fields = '__all__'
    labels = {'name': 'nome', 'address': 'endereço'}


class EditStoreForm(forms.ModelForm):
  class Meta:
    model = Store
    fields = '__all__'
    labels = {'name': 'nome', 'address': 'endereço'}


class AddGiftVoucherForm(forms.ModelForm):
  class Meta:
    model = GiftVoucher
    fields = ['bar_code', 'discount_price', 'source_store', 'store_used', 'status_bar_code']
    labels = {'bar_code': 'codigo de barra', 
              'discount_price': 'preço de desconto', 
              'source_store': 'loja origem', 
              'store_used': 'loja destino', 
              'status_bar_code': 'status'}


class EditGiftVoucherForm(forms.ModelForm):
  class Meta:
    model = GiftVoucher
    fields = ['bar_code', 'discount_price', 'source_store', 'store_used', 'status_bar_code']
    labels = {'bar_code': 'codigo de barra', 
              'discount_price': 'preço de desconto', 
              'source_store': 'loja origem', 
              'store_used': 'loja destino', 
              'status_bar_code': 'status'}
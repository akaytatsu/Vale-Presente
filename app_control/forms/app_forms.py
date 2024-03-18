from django import forms
from user_control.models import CustomUser
from ..models import Store, GiftVoucher
from django.forms import ModelChoiceField
from django.utils import timezone


class AddStoreForm(forms.ModelForm):
  class Meta:
    model = Store
    fields = ['name', 'address', 'email']
    labels = {'name': 'nome', 'address': 'endereço'}


class EditStoreForm(forms.ModelForm):
  class Meta:
    model = Store
    fields = '__all__'
    labels = {'name': 'nome', 'address': 'endereço'}


class AddGiftVoucherForm(forms.ModelForm):
  class Meta:
    model = GiftVoucher
    fields = ['source_store', 'discount_price', 'bar_code']
    labels = {'discount_price': 'valor do vale cartão', 
              'source_store': 'loja origem',
              'bar_code': 'código de barra'}
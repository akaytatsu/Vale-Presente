from django.db import models
from user_control.models import CustomUser
from user_control.views import add_user_activity

class Store(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_by = models.ForeignKey(
        CustomUser, null=True, related_name="description", on_delete=models.SET_NULL)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['id']
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.old_name = self.name
  
  def save(self, *args, **kwargs):
    action = f'Adicionado nova loja: {self.name}'
    if self.pk is not None:
        action = f'Atualizado o nome da loja {self.old_name} para {self.name}'
        super().save(*args, **kwargs)
        #add_user_activity()
  
  def delete(self, *args, **kwargs):
    created_by = self.created_by
    action = f'Deletado a loja: {self.name}'
    super().delete(*args, **kwargs)
    #add_user_activity()

  def __str__(self):
    return self.name

class GiftVoucher(models.Model):
  bar_code = models.CharField(max_length=100, unique=True)
  discount_price = models.DecimalField(max_digits=6, decimal_places=2)
  source_store = models.ForeignKey(Store, related_name='vales_origem', on_delete=models.CASCADE)
  store_used = models.ForeignKey(Store, related_name='vales_utilizados', on_delete=models.CASCADE, null=True, blank=True)
  usage_date = models.DateField(null=True, blank=True)
  purchase_date = models.DateField(null=True, blank=True)
  status_bar_code = models.BooleanField(default=False)

  def __str__(self):
      return self.bar_code
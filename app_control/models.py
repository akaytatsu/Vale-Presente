from django.db import models
from user_control.models import CustomUser, Store
from user_control.views import add_user_activity
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def validate_length(value):
  if len(value) < 12:
    raise ValidationError(
      _('O valor %(value)s deve ter 13 caracteres.'),
      params={'value': value},
    )

class GiftVoucher(models.Model):
  discount_price = models.DecimalField(max_digits=6, decimal_places=2)
  source_store = models.ForeignKey(Store, related_name='vales_origem', on_delete=models.CASCADE)
  usage_date = models.DateField(null=True, blank=True)
  bar_code = models.CharField(unique=True, null=True, max_length=13, validators=[validate_length])
  status_bar_code = models.BooleanField(default=False)
  store_used = models.ForeignKey(Store, related_name='vales_utilizados', on_delete=models.CASCADE, null=True, blank=True)
  purchase_date = models.DateField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['created_at']
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    super().delete(*args, **kwargs)

  def __str__(self):
    return f'{self.source_store} | {str(self.discount_price)}'
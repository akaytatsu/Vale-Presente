from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GiftVoucher(models.Model):
    bar_code = models.CharField(max_length=100, unique=True)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    source_store = models.ForeignKey(Store, related_name='vales_origem', on_delete=models.CASCADE)
    store_used = models.ForeignKey(Store, related_name='vales_utilizados', on_delete=models.CASCADE, null=True, blank=True)
    usage_date = models.DateField(null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.bar_code
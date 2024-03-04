from django.contrib import admin
from .models import Store, GiftVoucher

admin.site.register((Store, GiftVoucher,))

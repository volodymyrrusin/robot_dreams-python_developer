from django.contrib import admin
from purchase.models import Purchase

# Register your models here.


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'book_id', 'date')

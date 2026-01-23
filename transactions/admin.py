from django.contrib import admin
from . import models


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'customer', 'value', 'created_at', 'updated_at')
    search_fiels = ('customer')


admin.site.register(models.Transaction, TransactionAdmin)

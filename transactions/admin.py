from django.contrib import admin
from . import models


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'customer', 'value')
    search_fiels = ('customer')


admin.site.register(models.Transaction, TransactionAdmin)

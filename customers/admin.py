from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf_cnpj', 'email', 'phone',)
    search_fields = ('name', 'cpf_cnpj',)
    list_filter = ('name',)
    orderning = ('name',)


admin.site.register(models.Customer, CustomerAdmin)

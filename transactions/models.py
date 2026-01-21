import uuid
from django.db import models
from customers.models import Customer


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    # file1 = models.FieldFile()
    # file2 = models.FieldFile()
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='customer',
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.description

from rest_framework import serializers
from .models import Transaction
from customers.models import Customer


# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = ['id', 'description', 'value', 'file1', 'file2', 'customer']

class TransactionSerializer(serializers.ModelSerializer):
    customer_email = serializers.EmailField(write_only=True)
    customer_name = serializers.CharField(write_only=True, required=False)
    customer_phone = serializers.CharField(write_only=True, required=False)
    customer_cpf_cnpj = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Transaction
        fields = [
            "description",
            "value",
            "file1",
            "file2",
            "customer_email",
            "customer_name",
            "customer_phone",
            "customer_cpf_cnpj",
        ]

    def create(self, validated_data):
        cpf_cnpj = validated_data.pop("customer_cpf_cnpj")

        customer_data = {
            "name": validated_data.pop("customer_name", "Cliente não informado"),
            "phone": validated_data.pop("customer_phone", ""),
            "email": validated_data.pop("customer_email", ""),
        }

        customer, created = Customer.objects.get_or_create(
            cpf_cnpj=cpf_cnpj,
            defaults=customer_data
        )

        if not created:
            updated = False
            for field, value in customer_data.items():
                if value and getattr(customer, field) != value:
                    setattr(customer, field, value)
                    updated = True
            if updated:
                customer.save()

        return Transaction.objects.create(
            customer=customer,
            **validated_data
        )

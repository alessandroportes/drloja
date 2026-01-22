from rest_framework import generics

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

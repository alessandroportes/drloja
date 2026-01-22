from rest_framework import generics

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionsCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

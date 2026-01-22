from django.urls import path
from . import views


urlpatterns = [
  path(
    'transactions/',
    views.TransactionsCreate.as_view(),
    name='transactions-create',
  )
]

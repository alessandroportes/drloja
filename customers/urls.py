from django.urls import path
from . import views


urlpatterns = [
  path('customers/', views.CustomersCreate.as_view(), name='customers-create')
]

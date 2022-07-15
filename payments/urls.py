from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.initiate_payment, name='process'),
    path('verify/<slug:ref>/', views.verify_payment, name='verify-payment')
]
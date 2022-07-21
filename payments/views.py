from re import template
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings

from payments.models import Payment
from django.http import HttpResponse, HttpRequest
from orders.models import Order
from cart.cart import Cart

def initiate_payment(request: HttpRequest) -> HttpResponse:
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.order_total
    payment = Payment()
    payment.amount = total_cost
    payment.email = order.email
    payment.save()
    return render(request, 'pages/make_payment.html', {'payment':payment, 'order':order, 'total_cost':total_cost, 'PAYSTACK_PUBLIC_KEY':settings.PAYSTACK_PUBLIC_KEY})

def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verified')
    messages.error(request, 'Verification Failed')
    template_name = 'pages/index.html'
    return render(request, template_name)
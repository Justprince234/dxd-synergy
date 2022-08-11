from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from cart.cart import Cart
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

import weasyprint

def order_create(request):
    cart = Cart(request)
    current_site = get_current_site(request)
    if request.method == 'POST':
        carttotal = cart.get_total_price()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        payment_option = request.POST.get('payment_option')
        order = Order.objects.create(first_name=first_name, last_name=last_name, phone=phone, address=address, email=email, state=state,
        postal_code=postal_code, country=country, payment_option=payment_option)
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount
            order.amount = cart.get_total_price()
        order.amount = cart.get_total_price()
        order.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],price=item['price'],quantity=item['quantity'])

        # clear the cart
        cart.clear()
        # set the order in the session
        request.session['order_id'] = order.id
        message = render_to_string('pages/invoice.html', {
            'order': order,
            'domain':current_site.domain
        })
        mail_subject = 'DXD SYNERGY ORDER INFORMATION'
        recipient_list = order.email
        from_email = 'contact@dxd-synergy.com'
        send_mail(mail_subject, str(message), from_email, [str(recipient_list)], fail_silently=False)
        # redirect for payment
        if payment_option == 'pay_on_delivery':
            return redirect('orders:success')
        elif payment_option == 'paystack':
            return redirect('payment:process')
    return render(request, 'pages/checkout.html', {'carttotal': carttotal})

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    template_name = 'pages/detail.html'
    return render(request,template_name,{'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('pages/invoice.html', {'order':order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
    
	weasyprint.HTML(string=html).write_pdf(response)
	return response


def success(request, ):
    "Renders the invoice html page"
    request.session.flush()
    template_name = 'pages/success.html'
    return render(request, template_name)

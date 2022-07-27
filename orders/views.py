from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from payments.models import Payment
from cart.cart import Cart

import weasyprint

def order_create(request):
    cart = Cart(request)
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
        order = Order.objects.create(first_name=first_name, last_name=last_name, phone=phone, address=address, email=email, state=state,
        postal_code=postal_code, country=country)
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount
            order.amount = cart.get_total_price_after_discount()
        order.amount = cart.get_total_price()
        order.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],price=item['price'],quantity=item['quantity'])

        # clear the cart
        cart.clear()
        # set the order in the session
        request.session['order_id'] = order.id
        # redirect for payment
        return redirect('payment:process')
    return render(request, 'pages/checkout.html', {'carttotal': carttotal})

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    template_name = 'pages/detail.html'
    return render(request,template_name,{'order': order})

@staff_member_required
def admin_order_pdf(_request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('pages/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])

    return response

# def success(request):
#     template_name ='pages/success'
#     return render (request, template_name)
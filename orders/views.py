from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, Order
from cart.cart import Cart

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
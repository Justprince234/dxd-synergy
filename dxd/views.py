from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django.http import Http404
from django.db.models import Q


from .models import Category, Product, Career
from orders.models import Order
from cart.forms import CartAddProductForm

# Create your views here.

def home(request):
    """Displays the index page."""
    template_name = 'pages/index.html'
    context = {'categories': Category.objects.all()}
    return render(request, template_name, context)

def track_order(request):
    "Renders the order tracking page."
    template_name = 'pages/DXDtrack.html'
    if 'q':
        q = request.GET.get('q', False)
        orders = Order.objects.filter(order_number__icontains=q)
        return render(request,"pages/DXDtrack.html", {'orders': orders})
    return render(request, template_name)

def corporate_responsibility(request):
    "Renders the corporate reponsibility page."
    template_name = 'pages/corp-responsibility.html'
    return render(request, template_name)

def investor_site(request):
    "Renders the investor's site page"
    template_name = 'pages/investors-site.html'
    return render(request, template_name)

def gift_vouchers(request):
    "Renders the gift/voucher page"
    template_name = 'pages/gifts-vouchers.html'
    return render(request, template_name)

def career_page(request):
    "Renders the career page"
    careers = Career.objects.filter(available=True)
    template_name = 'pages/dxd-careers.html'
    context = {
        'careers': careers
    }
    return render(request, template_name, context)

def about_us(request):
    "Renders the about us page."
    template_name = 'pages/about.html'
    return render(request, template_name)

def black_friday(request):
    """ A view to show black friday items"""
    black_fridays = Product.objects.filter(black_friday=True)
    template_name = "pages/black-friday.html"
    return render (request, template_name, {'black_fridays': black_fridays})

def new_arrival(request):
    """ Renders new arrival items"""
    new_arrival = Product.objects.filter(new_arrival=True)
    template_name = "pages/new-arrival.html"
    return render (request, template_name, {'new_arrival': new_arrival})

def best_sellers(request):
    """ Renders best_sellers items"""
    best_seller= Product.objects.filter(best_seller=True)
    template_name = "pages/best_seller.html"
    return render (request, template_name, {'best_seller': best_seller})

def summer(request):
    """ Renders summer items"""
    summer= Product.objects.filter(summer=True)
    template_name = "pages/best_seller.html"
    return render (request, template_name, {'summer': summer})

def travels(request):
    """ Renders travels items"""
    travels= Product.objects.filter(travels=True)
    template_name = "pages/travels.html"
    return render (request, template_name, {'travels': travels})

def gifts(request):
    """ Renders gifts items"""
    gifts= Product.objects.filter(gift=True)
    template_name = "pages/gifts.html"
    return render (request, template_name, {'gifts': gifts})

def terms_condition(request):
    """ Renders terms and conditions"""
    template_name = "pages/Terms_Condition.html"
    return render (request, template_name)

def mobile_apps(request):
    """ Renders mobile apps page"""
    template_name = "pages/mobile-apps.html"
    return render (request, template_name)

def delivery_returns(request):
    "Renders delivery page"
    template_name = 'pages/delivery.html'
    return render(request, template_name)

def search(request):
    q = request.GET['q']
    products = Product.objects.filter(name__icontains=q)
    return render(request,'pages/search.html', {'products': products})

def product(request, slug):
    """ A view to show individual product details """

    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category).exclude(slug=slug)[:4]
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'related_products': related_products,
        'cart_product_form': cart_product_form
    }

    return render(request, 'pages/productDescription.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    template_name = 'pages/shopping.html'

    context = {
        'products': products,
        'category':category
    }

    return render(request, template_name, context)
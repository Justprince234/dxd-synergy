from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django.http import Http404
from django.db.models import Q


from .models import Category, Product, Career
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
    return render(request, template_name)

def corporate_responsibility(request):
    "Renders the corporate reponsibility page."
    template_name = 'pages/corp-responsibility.html'
    return render(request, template_name)

def investor_site(request):
    "Renders the investor's site page"
    template_name = 'pages/investors-site.html'
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
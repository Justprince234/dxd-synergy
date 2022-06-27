from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import Http404

from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

def home(request):
    """Displays the index page."""
    template_name = 'index.html'
    context = {'categories': Category.objects.all()}
    return render(request, template_name, context)

def products(request):
    template_name = "pages/products.html"
    return render(request, template_name)

def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    template_name = 'pages/products.html'
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, template_name, {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'gallery/art/product.html', {'product': product, 'cart_product_form': cart_product_form})
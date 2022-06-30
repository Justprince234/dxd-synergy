from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django.http import Http404
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages


from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

def home(request):
    """Displays the index page."""
    template_name = 'index.html'
    context = {'categories': Category.objects.all()}
    return render(request, template_name, context)

def products(request):
    template_name = "pages/productDescription.html"
    return render(request, template_name)

def products_list(request, category_slug=None):
    category = None
    query = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    template_name = 'pages/shopping.html'
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        print(categories)

    return render(request, template_name, {'category': category, 'categories': categories, 'products': products})

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.filter(available=True)
    query = None
    categories = Category.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    template_name = 'pages/shopping.html'

    print(categories)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, template_name, context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/productDescription.html', {'product': product, 'cart_product_form': cart_product_form})

def product(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'pages/productDescription.html', context)
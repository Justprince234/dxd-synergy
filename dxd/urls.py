from unicodedata import name
from django.urls import path
from . import views

app_name = 'dxd'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_list, name='product_list'),
    path('product/', views.products, name='product'),
    path('<slug:category_slug>/', views.products_list, name='products_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
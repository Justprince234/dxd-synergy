from unicodedata import name
from django.urls import path
from . import views

app_name = 'dxd'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('category/<slug:category_slug>/', views.category_list, name='products_list_by_category'),
]
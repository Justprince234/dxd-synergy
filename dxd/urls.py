
from django.urls import path
from . import views

app_name = 'dxd'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('track-order/', views.track_order, name='track-order'),
    path('corporate-responsibility/', views.corporate_responsibility, name='corporate-responsibility'),
    path('investor-site/', views.investor_site, name='investor-site'),
    path('careers/', views.career_page, name='careers'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('category/<slug:category_slug>/', views.category_list, name='products_list_by_category'),
]
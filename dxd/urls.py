
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
    path('black-friday/', views.black_friday, name='black-friday'),
    path('new-arrival/', views.new_arrival, name='new-arrival'),
    path('best-seller/', views.best_sellers, name='best-seller'),
    path('mobile-apps/', views.mobile_apps, name='mobile-apps'),
    path('coupons/', views.gift_vouchers, name='coupons'),
    path('summer/', views.summer, name='summer'),
    path('gifts/', views.gifts, name='gifts'),
    path('help/', views.help, name='help'),
    path('travels/', views.travels, name='travels'),
    path('terms-conditions/', views.terms_condition, name='terms-conditions'),
    path('delivery-returns/', views.delivery_returns, name='delivery-returns'),
    path('search/', views.search, name='search'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('category/<slug:category_slug>/', views.category_list, name='products_list_by_category'),
]
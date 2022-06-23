from django.urls import path
from . import views

app_name = 'dxd'
urlpatterns = [
    path('', views.home, name='home')

]
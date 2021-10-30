from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('contact/',views.customers,name='customer'),
    path('about/',views.products, name='products'),
    path('library/',views.library, name='library'),
    path('library/writer/<int:writerId>',views.Bwriter, name='book')


    
]
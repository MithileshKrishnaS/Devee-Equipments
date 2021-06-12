from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('products/', views.products, name='products'),
    path('pro/', views.pro, name='pro'),
    path('customer/', views.customer, name='customer'),
    path('contact', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('view/<int:id>', views.view, name='view'),
    path('check/<int:id>', views.check, name='check'),
   ]
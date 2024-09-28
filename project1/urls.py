"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from e_commerce import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.product_list, name='product_list'),  # Product list
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Product detail
    path('cart/', views.view_cart, name='view_cart'),  # View cart
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('signup/', views.signup, name='signup'),  # Signup
    path('checkout/', views.checkout, name='checkout'),  # Checkout
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),  # Order confirmation
]

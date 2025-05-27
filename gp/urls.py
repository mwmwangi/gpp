"""
URL configuration for business project.

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
from . import views
from django.contrib.auth import views as auth_views

from .views import mpesa_callback, mpesa_payment

urlpatterns = [
    path('index/',views.index,name='index'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('service/',views.service,name='service'),

    # path('starter_page/',views.starterpage,name='starterpage'),
    path('commercelist/',views.commercelist,name='commercelist'),
    path('updatecommerce/<int:id>/', views.updatecommerce, name='updatecommerce'),
    path('deletecommerce/<int:id>/', views.deletecommerce, name='deletecommerce'),
    path('commerceapi/',views.commerceapi,name='commerceapi'),
    path('signup/',views.signup_view,name='signup'),
    path(
        'login_view/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path("subscribe/", views.subscribe, name="subscribe"),

    path('mpesa/payment/', mpesa_payment, name='mpesa_payment'),

    # ... your other patterns
    path('mpesa/callback/', mpesa_callback, name='mpesa_callback'),
]

    # Add other URL patterns as needed




    # path('cookie/',views.buy_cookie_view,name='buy_cookie'),




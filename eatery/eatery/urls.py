"""eatery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from customer.views import Index, HomeMenu, BreakfastMenu, LunchMenu, DinnerMenu, About

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('menu/', HomeMenu.as_view(), name='home_menu'),
    path('menu/', BreakfastMenu.as_view(), name='breakfast_menu'),
    path('menu/', LunchMenu.as_view(), name='lunch_menu'),
    path('menu/', DinnerMenu.as_view(), name='dinner_menu'),
    path('about/', About.as_view(), name='about'),
]

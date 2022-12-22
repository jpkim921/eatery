from django.shortcuts import render
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/index.html')

class HomeMenu(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/home_menu.html')
class BreakfastMenu(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/breakfast_menu.html')
class LunchMenu(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/lunch_menu.html')
class DinnerMenu(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/dinner_menu.html')

class About(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/about.html')
from enum import Enum

from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel

class MealType(Enum):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class HomeMenu(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'customer/home_menu.html')

    def post(self, request, *args, **kwargs):
        # meal = MealType()
        context = {}
        # print('meal_type', request.POST['meal_type'])
        meal_type = request.POST['meal_type']
        context['meal'] = meal_type
        # search db based on request.POST['meal_type']

        print(context)
        return render(request, 'customer/home_menu.html', context=context)



        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')

        # return render(request, self.template_name, {'form': form})


class BreakfastMenu(View):
    def get(self, request, *args, **kwargs):
        context = {
            'menu_items': [
                {
                    'name': 'Lo Mein'
                },
                {
                    'name': 'Gen Tso'
                },
                {
                    'name': 'Dumplings'
                },
            ]
        }
        return render(request, 'customer/breakfast_menu.html', context=context)
class LunchMenu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/lunch_menu.html')
class DinnerMenu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/dinner_menu.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entrees = MenuItem.objects.filter(category__name__contains='Entree')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        context = {
            'appetizers': appetizers,
            'entrees': entrees,
            'desserts': desserts,
            'drinks': drinks,
        }
        print('context', context)
        return render(request, 'customer/order.html', context=context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }
        price = 0
        item_ids = []

        items = request.POST.getlist('items[]')

        # iterate through items and get the menu item and price from db
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item)) 
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)
            price += menu_item.price
            item_ids.append(menu_item.pk)
        

        # create the order
        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'customer/order_confirmation.html', context=context)
        


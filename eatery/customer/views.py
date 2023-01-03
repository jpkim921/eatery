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
        meal_type: str = request.POST['meal_type']
        context['meal'] = meal_type.upper()

        # search db based on request.POST['meal_type']

        menu_items = MenuItem.objects.filter(meal_time__name=meal_type)
        print("menu_items", menu_items)

        # context['menu_items'] = menu_items
        context['appetizer'] = menu_items.filter(category__name="Appetizer")
        context['entree'] = menu_items.filter(category__name="Entree")
        context['dessert'] = menu_items.filter(category__name="Dessert")
        context['drink'] = menu_items.filter(category__name="Drink")
        # print('post context', context)

        return render(request, 'customer/home_menu.html', context=context)

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
        return render(request, 'customer/order.html', context=context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }
        price = 0
        item_ids = []

        items = request.POST.getlist('items[]')
        print("items", items)

        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        # iterate through items and get the menu item and price from db
        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item)) 
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)
            price += menu_item.price
            item_ids.append(menu_item.pk)
            # print(order_items['items'])
        

        # create the order
        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zipcode=zipcode,
            )
        order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'customer/order_confirmation.html', context=context)
        # return render(request, 'customer/order_confirmation.html', context={})
        


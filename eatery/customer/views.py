from enum import Enum

from django.shortcuts import render
from django.views import View

class MealType(Enum):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'

# Create your views here.
class Index(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/index.html')

class HomeMenu(View):

    def get(self, request, * args, **kwargs):
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
    def get(self, request, * args, **kwargs):
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
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/lunch_menu.html')
class DinnerMenu(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/dinner_menu.html')

class About(View):
    def get(self, request, * args, **kwargs):
        return render(request, 'customer/about.html')
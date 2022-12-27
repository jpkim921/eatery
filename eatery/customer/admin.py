from django.contrib import admin
from .models import MenuItem, Category, MealTime, OrderModel

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(MealTime)
admin.site.register(OrderModel)
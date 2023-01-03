from django.db import models

# Create your models here.

class MenuItem(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item') # apetizer, entree, dessert, drink
    image = models.ImageField(upload_to='menu_images')
    meal_time = models.ManyToManyField('MealTime', related_name='item') # apetizer, entree, dessert, drink
    # pub_date = models.DateField(auto_now_add=True)
    # allergens = 

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class MealTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=10, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
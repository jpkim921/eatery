from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator


from customer.models import OrderModel


# Create your views here.

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):

    
    def get(self, request, *args, **kwargs):

        paginate_by = 9

        # get all orders for today
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)
        paginator = Paginator(orders, per_page=paginate_by)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)

        # loop over today's orders and get total revenue
        revenue = 0
        for order in orders:
            revenue += order.price
    
        # get total # order and revenue
        context = {
            'page_object': page_object,
            'total_revenue': revenue,
            'total_orders': len(orders),
        }

        print(context)


        return render(request, 'restaurant/dashboard.html', context=context)


    def test_func(self) -> bool:
        """
        This functions is used by the UserPassesTestMixin and checks
        whether or not the user is allowed in the dashboard.
        """
        return self.request.user.groups.filter(name='Staff').exists()



class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        items = order.items.all()
        print(items)
        context = {
            'order': order,
            'items': items,
        }
        return render(request, 'restaurant/order-details.html', context=context)
    
    def test_func(self) -> bool:
        """
        This functions is used by the UserPassesTestMixin and checks
        whether or not the user is allowed in the dashboard.
        """
        return self.request.user.groups.filter(name='Staff').exists()
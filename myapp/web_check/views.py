from django.shortcuts import render
from django.views.generic import ListView
from api_food.models import Customer


class UserDetailView(ListView):

    model = Customer
    template_name = 'customer_list.html'
    queryset = 'users'
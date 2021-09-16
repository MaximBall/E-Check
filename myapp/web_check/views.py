from django.shortcuts import render
from django.views.generic import View
from api_food.models import Customer


class HomePageView(View):

    def get(self, request):

        users = Customer.objects.first()
        print(users)
        context = {"users": users}
        return render(request, "customer_list.html", context)
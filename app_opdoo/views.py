#sw_vehicle_search


from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from app_opdoo.forms import LoginForm
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from app_opdoo.models import *
from app_opdoo import homework_6

class Login(LoginView):
    success_url = reverse_lazy('CustomerList')
    template_name = 'Login.html'
    form_class = LoginForm
class Logout(LogoutView):
    next_page = 'Login'


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'Index.html'

    def get(self, request, *args, **kwargs):

        total_net_array = []


        data = {}

        return render(request, self.template_name, data)


class sw_vehicle_search(TemplateView):
    template_name = 'sw_vehicle_search.html'

    def get(self, request, *args, **kwargs):

        total_net_array = []

        customer_number = CustomerModel.objects.all().count()
        print("customer_number",customer_number)

        data = {'total_net': len(total_net_array),
                'currente_date': datetime.now(),
                'customer_number':customer_number}

        return render(request, self.template_name, data)
    
    def post(self, request, **kwargs):
        cargo_capacity = request.POST.get("cargo_capacity")
        max_speed = request.POST.get("max_speed")
        my_data = request.POST.get("cost")

        #result_list =  homework_6.sw_vehicle_search(755, 128, 252850)
        result_list =  homework_6.sw_vehicle_search(cargo_capacity, max_speed, my_data)

        print(result_list)

        # do something with your data
        context = {"result_list":result_list,
                    "result_list_len":len(result_list)}  #  set your context
        return super(TemplateView, self).render_to_response(context)
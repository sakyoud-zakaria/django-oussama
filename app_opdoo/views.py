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


        data = {}

        return render(request, self.template_name, data)
    
    def post(self, request, **kwargs):
        cargo_capacity = int(request.POST.get("cargo_capacity"))
        max_speed = int(request.POST.get("max_speed"))
        my_data = int(request.POST.get("cost"))

        #result_list =  homework_6.sw_vehicle_search(755, 128, 252850)
        result_list =  homework_6.sw_vehicle_search(cargo_capacity, max_speed, my_data)

        print(result_list)

        # do something with your data
        context = {"result_list":result_list,
                    "result_list_len":len(result_list)}  #  set your context
        return super(TemplateView, self).render_to_response(context)



class starship_piloted_species(TemplateView):
    template_name = 'starship_piloted_species.html'

    def get(self, request, *args, **kwargs):

        data = {}

        return render(request, self.template_name, data)
    
    def post(self, request, **kwargs):
        name = str(request.POST.get("name"))

        #print(starship_piloted_species('Death Star'))
        #print(starship_piloted_species('Jedi starfighter'))        

        result_list =  homework_6.starship_piloted_species(name)

        print(result_list)

        # do something with your data
        context = {"result_list":result_list,
                    "result_list_len":len(result_list)}  #  set your context
        return super(TemplateView, self).render_to_response(context)





class wear_a_jacket(TemplateView):
    template_name = 'wear_a_jacket.html'

    def get(self, request, *args, **kwargs):

        data = {'result_list': None}

        return render(request, self.template_name, data)
    
    def post(self, request, **kwargs):
        name = str(request.POST.get("name"))

        # wear_a_jacket('00653')
        result_list =  homework_6.wear_a_jacket(name)

        print(result_list)

        # do something with your data
        context = {"result_list":result_list}  #  set your context
        return super(TemplateView, self).render_to_response(context)



class past_weather(TemplateView):
    template_name = 'past_weather.html'

    def get(self, request, *args, **kwargs):

        data = {'result_list': None}

        return render(request, self.template_name, data)
    
    def post(self, request, **kwargs):
        days = int(request.POST.get("days"))
        hours = int(request.POST.get("hours"))
        minutes = int(request.POST.get("minutes"))
        us_zip = str(request.POST.get("us_zip"))

        # wear_a_jacket('00653')
        #print("past_weather : ", past_weather(3, 8, 54,"99588"))
        #Days = 3, Hours = 8, Minutes = 54, Zip = 99588
        result_list =  homework_6.past_weather(days, hours, minutes, us_zip)

        print(result_list)

        # do something with your data
        context = {"result_list":result_list}  #  set your context
        return super(TemplateView, self).render_to_response(context)


class cat_language(TemplateView):
    template_name = 'cat_language.html'

    def get(self, request, *args, **kwargs):

        data = {'result_list': None}

        return render(request, self.template_name, data)
    
    def post(self, request, **kwargs):

        breed = str(request.POST.get("breed"))
        language = str(request.POST.get("language"))

        # cat_language('colorpoint shorthair', 'nn')
        result_list =  homework_6.cat_language(breed, language)

        print(result_list)

        # do something with your data
        context = {"result_list":result_list}  #  set your context
        return super(TemplateView, self).render_to_response(context)



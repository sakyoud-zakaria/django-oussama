from django.contrib import admin
from django.urls import path, include

from app_opdoo.views import *

urlpatterns = [

    path('', Login.as_view(), name="Login"),
    path('Logout/', Logout.as_view(), name="Logout"),
    path('Index/', Index.as_view(), name="Index"),
    path('sw_vehicle_search/', sw_vehicle_search.as_view(), name="sw_vehicle_search"),
    path('sw_vehicle_search/search/', sw_vehicle_search.as_view(), name="sw_vehicle_search/search/"),
    path('starship_piloted_species/', starship_piloted_species.as_view(), name="starship_piloted_species"),
    path('starship_piloted_species/search/', starship_piloted_species.as_view(), name="starship_piloted_species/search/"),
    

]

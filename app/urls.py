from django.urls import path
from .views import home, api_home

urlpatterns = [
    path('', home, name='home'),
    path('home/', api_home, name='home'),
   
]


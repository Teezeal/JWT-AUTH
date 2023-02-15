from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse(" What The Fuck ! ")

@api_view(['GET'])
def api_home(request):
    context = {"data":"What the Fuck are you doing on my Page !"}
    return Response(context)
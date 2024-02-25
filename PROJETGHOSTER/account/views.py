from django.shortcuts import render
from django.http import Http404,HttpResponse
# Create your views here.

def login_app(request):
    return HttpResponse("Bonjour charia")
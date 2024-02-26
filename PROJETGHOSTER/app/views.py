from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context={'message' : "message"}
    templet=loader.get_template("app/index.html")
    
    return render(request,templet,context)
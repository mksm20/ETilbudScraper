from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

def index(request):
    return render(request, 'index.html')
# Create your views here.
def shoplist(request):
    return render(request, 'shoplist.html')

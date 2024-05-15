from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "core/index.html", {'products':products})
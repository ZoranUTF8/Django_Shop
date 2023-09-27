from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def indexPage(request):
    allProducts = Product.objects.all()
    return render(request, "indexPage.html", {"allProducts": allProducts})


def newProducts(request):
    return HttpResponse("Ola from here")

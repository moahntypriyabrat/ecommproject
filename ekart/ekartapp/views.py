from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.


def home(request):
    products = Product.objects.all().filter(is_available=True)
    return render(request, 'ekartapp/index.html',context={'products': products, })


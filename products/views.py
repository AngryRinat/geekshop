from django.shortcuts import render
import json

# Create your views here.
def index(request):
    context = {
        "title": "Geekshop - главная страница"
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open('products/fixtures/data.json') as outfile:
        products_json = json.load(outfile)
    context = {
        "title": "Geekshop - продукты",
        "products": products_json
    }
    return render(request, 'products/products.html', context)

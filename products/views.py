from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title": "Geekshop - главная страница"
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        "title": "Geekshop - продукты"
    #     "products": [
    #     {'name":   , "price":  , "description":  , "img":}
    # ]
    }
    return render(request, 'products/products.html', context)

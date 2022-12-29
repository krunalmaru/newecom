from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    product = Product.get_all_products()
    context = {'product':product}
    print(product)
    return render(request, 'shop/home.html',context)
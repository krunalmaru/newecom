from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.hashers import check_password,make_password
from shop.models import Product,Category,Customer

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_ids(ids)
        return render(request,'shop/cart.html',{'products':products})


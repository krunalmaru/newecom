from django.shortcuts import render
from .models import Product,Category
# Create your views here.
def home(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_products_by_categoryid(categoryID)
    else:
        product = Product.get_all_products()
    context = {'product':product,'categories':categories}
    return render(request, 'shop/home.html',context)
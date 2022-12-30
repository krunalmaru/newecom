from django.shortcuts import render,HttpResponse
from .models import Product,Category,Customer
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

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        error_message = None
        if (not firstname):
            error_message = 'First Name required'
        elif(len(firstname)<3):
            error_message = 'First Name Should be 3 char required '
        elif(not lastname):
            error_message = 'Last Name required'
        elif len(lastname) < 4:
            error_message = 'Last Name Should be 4 char required'
        elif(not phone):
            error_message = 'phone Number required'
        elif len(phone) < 10:
            error_message = 'Phone Must be 10 Char'
           

        if  not error_message:
            customer = Customer(first_name=firstname,last_name=lastname,email=email,password=password,phone=phone)
            customer.register()
            return HttpResponse('signup success')
        else:
            return render(request, 'shop/signup.html',{'error':error_message})
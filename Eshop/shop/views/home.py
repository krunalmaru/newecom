from django.shortcuts import render,HttpResponse,redirect
from shop.models import Product,Category,Customer
from django.contrib.auth.hashers import check_password,make_password
from django.views import View
# Create your views here.
class MyHome(View):
    def get(self, request):
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_products_by_categoryid(categoryID)
        else:   
            product = Product.get_all_products()
        context = {'product':product,'categories':categories}
        print('you are',request.session.get('email'))
        return render(request, 'shop/home.html',context)

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1         
            else:
                cart[product] = 1
        else:
            cart ={}
            cart[product] = 1
        request.session['cart'] = cart    
        print(request.session['cart'])
        print(cart)
        print(product)
        return redirect('home')


    

# def validateCustomer(customer):
    # error_message = None
    # if (not customer.first_name):
    #         error_message = 'First Name required'
    # elif(len(customer.first_name)<3):
    #     error_message = 'First Name Should be 3 char required '
    # elif(not customer.last_name):
    #     error_message = 'Last Name required'
    # elif len(customer.last_name) < 4:
    #     error_message = 'Last Name Should be 4 char required'
    # elif(not customer.phone):
    #     error_message = 'phone Number required'
    # elif len(customer.phone) < 10:
    #     error_message = 'Phone Must be 10 Char'
    # elif(not customer.password):
    #     error_message = 'Password Must required'
    # elif customer.isExists():
    #     error_message = 'Customer Already Exist'    
    # return error_message

# def registeruser(request):
#     firstname = request.POST.get('first_name')
#     lastname = request.POST.get('last_name')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     phone = request.POST.get('phone')
#     value = {'firstname':firstname,'lastname':lastname,'email':email,'phone':phone}
#     error_message = None
#     customer = Customer(first_name=firstname,last_name=lastname,email=email,password=password,phone=phone)
#     error_message = validateCustomer(customer)
#     if  not error_message:
#         customer.password = make_password(customer.password)
#         customer.register()
#         return redirect('home')
#     else:

#         data = {
#             'error':error_message,
#             'values':value
#         }
#         return render(request,'shop/signup.html', data)

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'shop/signup.html')            
#     else:
#         return registeruser(request)


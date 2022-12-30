from django.shortcuts import render,HttpResponse,redirect
from shop.models import Product,Category,Customer
from django.contrib.auth.hashers import check_password,make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'shop/signup.html') 

    def post(self, request):
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        
        value = {'firstname':firstname,'lastname':lastname,'email':email,'phone':phone}

        error_message = None

        customer = Customer(first_name=firstname,last_name=lastname,email=email,password=password,phone=phone)
        error_message = self.validateCustomer(customer)


        if  not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:

            data = {
                'error':error_message,
                'values':value
            }
            return render(request,'shop/signup.html', data)

    def validateCustomer(self,customer):
        error_message = None
        if (not customer.first_name):
                error_message = 'First Name required'
        elif(len(customer.first_name)<3):
            error_message = 'First Name Should be 3 char required '
        elif(not customer.last_name):
            error_message = 'Last Name required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name Should be 4 char required'
        elif(not customer.phone):
            error_message = 'phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Must be 10 Char'
        elif(not customer.password):
            error_message = 'Password Must required'
        elif customer.isExists():
            error_message = 'Customer Already Exist'    
        return error_message

       

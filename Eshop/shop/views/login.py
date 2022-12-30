from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.hashers import check_password,make_password
from shop.models import Product,Category,Customer

class Login(View):
    def get(self, request):
        return render(request,'shop/login.html')


    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag =  check_password(password,customer.password)
            if flag:
                return redirect('home')
            else:
                error_message = 'Email or Password Invalid'
        else:
            error_message = 'Invalid creadential !!'    

        print(customer)
        print(email,password)
        return render(request, 'shop/login.html',{'error':error_message})


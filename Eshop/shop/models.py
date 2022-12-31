from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=150)
    price =  models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/img')

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in = ids)
        
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email) 
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
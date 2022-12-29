from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=150)
    price =  models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/img')

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    def __str__(self) -> str:
        return self.name
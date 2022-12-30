from django.contrib import admin
from .models import Product,Category,Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','category','image']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
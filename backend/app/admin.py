from django.contrib import admin
from .models import Product, Category, Supplier, User

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(User)

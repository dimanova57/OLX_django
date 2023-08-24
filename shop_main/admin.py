from django.contrib import admin

# Register your models here.
from .models import Product, Condition, Category, Place

admin.site.register(Product)
admin.site.register(Condition)
admin.site.register(Category)
admin.site.register(Place)

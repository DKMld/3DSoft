from django.contrib import admin
from djangoProject.products.models import Products, ProductsLikes, ProductsCart

admin.site.register(Products)
admin.site.register(ProductsLikes)
admin.site.register(ProductsCart)
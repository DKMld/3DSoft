from django.contrib import admin
from djangoProject.products.models import Products, ProductsLikes


admin.site.register(Products)
admin.site.register(ProductsLikes)
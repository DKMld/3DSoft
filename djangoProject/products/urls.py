from django.urls import path
from djangoProject.products import views as products_views

urlpatterns = [
    path('product_detail/', products_views.product_detail, name='product_detail'),

]
from django.urls import path
from djangoProject.products import views as products_views


urlpatterns = [
    path('product_detail/<slug:product_slug>', products_views.product_detail, name='product_detail'),
    path('add_to_cart/<slug:product_slug>', products_views.product_add_to_cart, name='product_add_to_cart'),
    path('products/<category>/<sub_category>/<sorting>', products_views.product_page, name='products_page'),
]

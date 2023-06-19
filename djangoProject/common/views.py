import requests
from django.shortcuts import render, get_object_or_404

from djangoProject.products.models import Products, ProductsCart, ProductsLikes


def home_page(request):
    current_user_location = get_current_user_location()

    new_products = Products.objects.filter().order_by('id')[:10]
    sale_products = Products.objects.filter(discount_percentage__gt=0).order_by('id')[:5]

    products_in_cart = None
    total_price_of_cart = None
    number_of_products_in_cart = None

    if request.user.is_authenticated:
        user = request.user

        products_in_cart = ProductsCart.objects.filter(user=user)
        total_price_of_cart = ProductsCart.total_price(current_user=user)
        number_of_products_in_cart = ProductsCart.total_products_in_user_cart(user)

    context = {
        'user_is_auth': request.user.is_authenticated,
        'current_user_location': current_user_location['country'],

        'new_products': new_products,
        'sale_products': sale_products,

        'products_in_cart': products_in_cart,
        'number_of_products_in_cart': number_of_products_in_cart,
        'total_cart_price': total_price_of_cart,
    }

    return render(request, 'common/home.html', context)


def wishlist(request):
    products_in_cart = None
    total_price_of_cart = None
    number_of_products_in_cart = None
    products_in_current_user_wishlist = None

    if request.user.is_authenticated:
        user = request.user
        products_in_cart = ProductsCart.objects.filter(user=user)
        total_price_of_cart = ProductsCart.total_price(current_user=user)
        number_of_products_in_cart = ProductsCart.total_products_in_user_cart(user)
        products_in_current_user_wishlist = ProductsLikes.objects.filter(user=request.user)

    context = {
        'user_is_auth': request.user.is_authenticated,

        'products_in_cart': products_in_cart,
        'number_of_products_in_cart': number_of_products_in_cart,
        'total_cart_price': total_price_of_cart,

        'products_in_wishlist': products_in_current_user_wishlist,
    }

    return render(request, 'common/wishlist.html', context)


def checkout(request):
    return render(request, 'product/product-single.html',)


def get_current_user_ip():
    response = requests.get(f'https://api64.ipify.org?format=json').json()

    return response['ip']


def get_current_user_location():
    ip_address = get_current_user_ip()

    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    location_data = {
        'ip': ip_address,
        'city': response.get('city'),
        'region': response.get('region'),
        'country': response.get('country_name'),
    }

    return location_data

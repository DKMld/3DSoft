import requests
from django.shortcuts import render

from djangoProject.products.models import Products, ProductsCart


def home_page(request):
    current_user_location = get_current_user_location()

    new_products = Products.objects.filter().order_by('id')[:10]
    sale_products = Products.objects.filter(discount_percentage__gt=0).order_by('id')[:5]

    products_in_cart = None
    total_price_of_cart = None

    if request.user.is_authenticated:
        products_in_cart = ProductsCart.objects.filter(user=request.user)
    print(products_in_cart)

    if request.user.is_authenticated:
        total_price_of_cart = ProductsCart.total_price(current_user=request.user)

    context = {
        'user_is_auth': request.user.is_authenticated,
        'current_user_location': current_user_location['country'],

        'new_products': new_products,
        'sale_products': sale_products,


        'products_in_cart': products_in_cart,
        'total_cart_price': total_price_of_cart,

    }

    return render(request, 'common/home.html', context)


def checkout(request):
    return render(request, 'product/product-single.html',)


# def product_search(request):
#     if request.method == 'GET':
#         products = Products.objects.filter().order_by('-id').all()
#         search_form = ProductSearchForm(request.GET)
#         search_pattern = None
#
#         if search_form.is_valid():
#             search_pattern = request.GET.get('search')
#
#         if search_pattern:
#             products = products.filter(product_name__icontains=search_pattern)
#
#         context = {
#             'user_is_auth': request.user.is_authenticated,
#             'products': products,
#             'products_count': products.count(),
#         }
#
#         return render(request, 'product_pages/product_search_page.html', context)
#
#




def get_current_user_ip():
    response = requests.get(f'https://api64.ipify.org?format=json').json()
    print(response['ip'])
    return response['ip']


def get_current_user_location():
    ip_address = get_current_user_ip()

    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    print(response)
    location_data = {
        'ip': ip_address,
        'city': response.get('city'),
        'region': response.get('region'),
        'country': response.get('country_name'),
    }

    return location_data

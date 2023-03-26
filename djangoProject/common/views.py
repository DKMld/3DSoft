import requests
from django.shortcuts import render

from djangoProject.products.models import Products


def home_page(request):
    current_user_location = get_current_user_location()

    new_products = Products.objects.filter().order_by('id')[:7]
    sale_products = Products.objects.filter(discount_percentage__gt=0).order_by('id')[:7]

    context = {
        'user_is_auth': request.user.is_authenticated,
        'current_user_location': current_user_location['country'],

        'new_products': new_products,
        'sale_products': sale_products,
    }

    return render(request, 'common/home.html', context)


def checkout(request):

    return render(request, 'common/checkout.html')


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

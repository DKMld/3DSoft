import requests
from django.shortcuts import render


def home_page(request):
    current_user_location = get_current_user_location()

    context = {
        'user_is_auth': request.user.is_authenticated,
        'current_user_location': current_user_location['country']

    }

    return render(request, 'common/home.html', context)


def checkout(request):

    return render(request, 'common/checkout.html')








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
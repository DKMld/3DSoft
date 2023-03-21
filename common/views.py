from django.shortcuts import render


def home_page(request):

    context = {
        'user_is_auth': request.user.is_authenticated
    }

    return render(request, 'common/home.html', context)


def checkout(request):

    return render(request, 'common/checkout.html')
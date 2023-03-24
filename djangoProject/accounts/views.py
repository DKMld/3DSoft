from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return None

        create_user = User.objects.create_user(username=username, email=email, password=password)
        create_user.save()

        return None

    return render(request, 'auth/signup.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home_page')

        return redirect('home_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')



def delete_user(request):
    pass
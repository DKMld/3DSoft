from django.urls import path

from accounts import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.register_user, name='user_register'),
    path('signin/', accounts_views.login_user, name='user_login'),

]
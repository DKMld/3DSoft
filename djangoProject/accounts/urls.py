from django.urls import path

from djangoProject.accounts import views as accounts_views

urlpatterns = [
    path('signup/', accounts_views.register_user, name='user_register'),
    path('signin/', accounts_views.login_user, name='user_login'),
    path('logout/', accounts_views.logout_user, name='user_logout'),

]
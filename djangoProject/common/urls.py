from django.urls import path
from djangoProject.common import views as common_views

urlpatterns = [
    path('', common_views.home_page, name='home_page'),
    path('checkout/', common_views.checkout, name='checkout'),

]
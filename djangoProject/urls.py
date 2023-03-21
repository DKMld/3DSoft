from django.contrib import admin
from django.urls import path, include
from common import urls as common_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(common_urls)),
    path('', include(accounts_urls)),
]


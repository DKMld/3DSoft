from django.contrib import admin
from django.urls import path, include

from djangoProject.common import urls as common_urls
from djangoProject.accounts import urls as accounts_urls
from djangoProject.products import urls as products_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(common_urls)),
    path('', include(accounts_urls)),
    path('', include(products_urls)),
]


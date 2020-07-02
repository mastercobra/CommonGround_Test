from django.contrib import admin
from django.urls import path
from product_api.product_api import ProductApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/create_products', ProductApi.as_view(), name="api_create_products"),
]

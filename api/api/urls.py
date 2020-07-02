from django.contrib import admin
from django.urls import path
from product_api.product_api import ProductApi, GetProductApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/bulk_insert', ProductApi.as_view(), name="api_create_products"),
    path('api/products', GetProductApi.as_view(), name="api_list_products"),

]

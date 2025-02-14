from django.urls import path
from .views import product_list, product_add, product_delete, order_list

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/add/', product_add, name='product_add'),
    path('products/delete/<int:id>/', product_delete, name='product_delete'),
    path('orders/', order_list, name='order_list'),
]
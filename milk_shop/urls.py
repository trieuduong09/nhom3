from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Trang quản trị Django
    path('', include('app_admin.urls')),  # Gắn URLs của app_admin vào hệ thống
]

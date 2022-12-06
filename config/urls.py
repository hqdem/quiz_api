from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/', include('quiz_api.urls')),
    re_path(r'api/v1/auth-token/', include('djoser.urls.authtoken')),
]

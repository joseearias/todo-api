from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('users/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]

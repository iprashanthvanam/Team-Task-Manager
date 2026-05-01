from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', lambda request: redirect('dashboard'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('projects.dashboard_urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    # REST API endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('accounts.api_urls')),
    path('api/', include('projects.api_urls')),
    path('api/', include('tasks.api_urls')),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, RegisterAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api-register'),
    path('', include(router.urls)),
]

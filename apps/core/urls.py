from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, EventViewSet


router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]

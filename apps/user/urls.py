from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.RoleCreateView.as_view(), name='role-create'),
    path('roles/<int:pk>/', views.RoleRetrieveView.as_view(), name='role-detail'),
]

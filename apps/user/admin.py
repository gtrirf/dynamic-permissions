from django.contrib import admin
from .models import APIAction, Role, CustomUser


@admin.register(APIAction)
class APIActionAdmin(admin.ModelAdmin):
    search_fields = ('api', 'action',)
    list_display = ('api_action_combined', 'action_name')

    def api_action_combined(self, obj):
        return f'{obj.api}_{obj.action}'
    api_action_combined.short_description = 'API_ACTION'


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role',)
    search_fields = ('role',)
    filter_horizontal = ('api_actions',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'role']
    list_filter = ['is_staff', 'is_active', 'role']
    search_fields = ['username', 'first_name', 'last_name', 'email']


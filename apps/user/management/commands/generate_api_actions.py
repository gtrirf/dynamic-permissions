import importlib
import inspect
from django.core.management.base import BaseCommand
from django.urls import URLPattern, URLResolver
from rest_framework.routers import DefaultRouter
from apps.user.models import APIAction
from apps.user.tools import API_ACTION_CHOICES
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate APIAction entries for each view and action type defined in routers or custom URL patterns.'

    def handle(self, *args, **options):
        APIAction.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing APIActions cleared.'))
        view_names = self.get_router_view_names() | self.get_path_view_names()
        self.create_api_actions(view_names)

    def get_router_view_names(self):
        view_names = set()

        for app in settings.INSTALLED_APPS:
            try:
                urls_module = importlib.import_module(f'{app}.urls')

                if hasattr(urls_module, 'router'):
                    router = urls_module.router
                    if isinstance(router, DefaultRouter):
                        for prefix, viewset, basename in router.registry:
                            view_name = getattr(viewset, 'start_name', None)
                            if view_name:
                                view_names.add(view_name.lower())

            except ModuleNotFoundError:
                continue

        self.stdout.write(self.style.SUCCESS(f'Found {len(view_names)} view names in routers.'))
        return view_names

    def get_path_view_names(self):
        view_names = set()

        for app in settings.INSTALLED_APPS:
            try:
                urls_module = importlib.import_module(f'{app}.urls')

                urlpatterns = getattr(urls_module, 'urlpatterns', [])
                for pattern in urlpatterns:
                    if isinstance(pattern, URLPattern):
                        view = pattern.callback
                        view_name = getattr(view, 'start_name', None)
                        if view_name:
                            view_names.add(view_name.lower())
                    elif isinstance(pattern, URLResolver):
                        nested_urlpatterns = pattern.url_patterns
                        for nested_pattern in nested_urlpatterns:
                            if isinstance(nested_pattern, URLPattern):
                                view = nested_pattern.callback
                                view_name = getattr(view, 'start_name', None)
                                if view_name:
                                    view_names.add(view_name.lower())
            except ModuleNotFoundError:
                continue

        self.stdout.write(self.style.SUCCESS(f'Found {len(view_names)} view names in URL paths.'))
        return view_names

    def create_api_actions(self, view_names):
        actions = [choice[0] for choice in API_ACTION_CHOICES]
        created_count = 0

        for view_name in view_names:
            for action in actions:
                api_action, created = APIAction.objects.get_or_create(api=view_name, action=action)
                if created:
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f'Created APIAction: {api_action}'))
                else:
                    self.stdout.write(self.style.WARNING(f'APIAction already exists: {api_action}'))

        if created_count == 0:
            self.stdout.write(self.style.ERROR('No APIAction entries were created.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Total APIAction entries created: {created_count}'))

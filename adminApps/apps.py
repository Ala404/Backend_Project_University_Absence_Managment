from django.apps import AppConfig


class AdminappsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminApps'
    
    def ready(self):
        from . import signals

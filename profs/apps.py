from django.apps import AppConfig


class ProfsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profs'
    
    
    def ready(self):
        import profs.signals

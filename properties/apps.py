from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'
    verbose_name = 'Property Listings' # A user-friendly name for the admin

    def ready(self):
        # Import your signals here so they are registered when the app loads
        import properties.signals
        print("Properties app signals loaded.") # For debugging/verification

from django.apps import AppConfig


class MflixConfig(AppConfig):
    name = "mflix"
    verbose_name = "MFlix"
    default_auto_field = "django_mongodb_backend.fields.ObjectIdAutoField"

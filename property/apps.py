"""
Module for property applications configurations.
"""
from django.apps import AppConfig

class PropertyConfig(AppConfig):
    """
    AppConfig class for the 'property' app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "property"

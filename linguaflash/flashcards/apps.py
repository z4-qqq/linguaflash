"""A Django application for managing flashcards."""
from django.apps import AppConfig


class FlashcardsConfig(AppConfig):
    """Configuration class for the flashcards Django application.
    
    This class defines metadata and configuration options for the flashcards app.
    It inherits from Django's base AppConfig class.
    
    Attributes:
        default_auto_field (str): Specifies the type of auto-created primary key field
            to use for models in this app. Set to 'django.db.models.BigAutoField'.
        name (str): The full Python path to the application, e.g. 'flashcards'.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flashcards'

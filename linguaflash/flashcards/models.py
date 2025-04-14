"""Database models for flashcards application."""
from django.db import models
from django.core.validators import MinLengthValidator

class Deck(models.Model):
    """Represents a collection of flashcards.
    
    Attributes:
        title (CharField): The name of the deck (1-100 characters)
        description (TextField): Optional description of the deck
        created_at (DateTimeField): When the deck was created (auto-set)
        updated_at (DateTimeField): When the deck was last updated (auto-updated)
    """
    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Flashcard(models.Model):
    """Represents a single flashcard with front/back content.
    
    Attributes:
        deck (ForeignKey): The deck this flashcard belongs to
        front_text (CharField): Main text shown on card front (1-200 chars)
        back_text (CharField): Main text shown on card back (1-200 chars)
        image (ImageField): Optional image for the flashcard
        created_at (DateTimeField): When card was created (auto-set)
        last_reviewed (DateTimeField): When card was last reviewed
        difficulty (IntegerField): Difficulty level (1=Easy, 2=Medium, 3=Hard)
    """
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='flashcards')
    front_text = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    back_text = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    image = models.ImageField(upload_to='flashcard_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(null=True, blank=True)
    difficulty = models.IntegerField(default=1, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])

    def __str__(self):
        return f"{self.front_text} - {self.back_text}"

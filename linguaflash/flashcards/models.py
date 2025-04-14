"""Models"""
from django.db import models
from django.core.validators import MinLengthValidator

class Deck(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='flashcards')
    front_text = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    back_text = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    image = models.ImageField(upload_to='flashcard_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(null=True, blank=True)
    difficulty = models.IntegerField(default=1, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])

    def __str__(self):
        return f"{self.front_text} - {self.back_text}"
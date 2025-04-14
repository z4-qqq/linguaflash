"""Forms for flashcards application."""
from django import forms
from .models import Deck, Flashcard

class DeckForm(forms.ModelForm):
    """Form for creating/editing Decks."""
    class Meta:
        model = Deck
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class FlashcardForm(forms.ModelForm):
    """Form for creating/editing Flashcards."""
    class Meta:
        model = Flashcard
        fields = ['deck', 'front_text', 'back_text', 'image', 'difficulty']

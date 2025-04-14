"""Flashcard urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('decks/', views.DeckListView.as_view(), name='deck_list'),
    path('decks/create/', views.create_deck, name='create_deck'),
    path('decks/<int:deck_id>/study/', views.study_deck, name='study_deck'),
    path('flashcards/', views.FlashcardListView.as_view(), name='flashcard_list'),
    path('flashcards/create/', views.create_flashcard, name='create_flashcard'),
]
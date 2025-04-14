"""Views"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Deck, Flashcard
from .forms import DeckForm, FlashcardForm
from django.core.paginator import Paginator

def home(request):
    return render(request, 'flashcards/home.html')

class DeckListView(ListView):
    model = Deck
    template_name = 'flashcards/deck_list.html'
    context_object_name = 'decks'

class FlashcardListView(ListView):
    model = Flashcard
    template_name = 'flashcards/flashcard_list.html'
    context_object_name = 'flashcards'

    def get_queryset(self):
        deck_id = self.kwargs.get('deck_id')
        if deck_id:
            return Flashcard.objects.filter(deck_id=deck_id)
        return Flashcard.objects.all()

def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deck_list')
    else:
        form = DeckForm()
    return render(request, 'flashcards/deck_form.html', {'form': form})

def create_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/flashcard_form.html', {'form': form})

def study_deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    flashcards = list(deck.flashcards.all())
    
    if not flashcards:
        return redirect('deck_list')
    
    current_index = request.session.get(f'deck_{deck_id}_index', 0)
    show_answer = request.GET.get('show_answer', 'false') == 'true'
    
    if 'next' in request.GET:
        current_index = (current_index + 1) % len(flashcards)
        show_answer = False
    elif 'prev' in request.GET:
        current_index = (current_index - 1) % len(flashcards)
        show_answer = False
    
    request.session[f'deck_{deck_id}_index'] = current_index
    
    flashcard = flashcards[current_index]
    
    return render(
        request, 
        'flashcards/study.html', 
        {
            'deck': deck,
            'flashcard': flashcard,
            'total_cards': len(flashcards),
            'current_index': current_index + 1,  # 1-based index for display
            'show_answer': show_answer,
            'progress': int(current_index / len(flashcards)) * 100 if len(flashcards) > 0 else 0
        }
    )
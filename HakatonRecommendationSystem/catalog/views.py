from django.shortcuts import render
from .models import Participant, Team, Skill

# Create your views here.


def index(request):
    # Generate counts of some of the main objects
    num_books = 3
    num_instances = 10

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances},
    )
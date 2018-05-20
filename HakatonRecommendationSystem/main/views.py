from django.shortcuts import render
from .models import Participant, Team, Skill

# Create your views here.


def registration(request):
    return render(
        request,
        'registration.html',
    )


def main(request):
    return render(
        request,
        'main.html',
    )

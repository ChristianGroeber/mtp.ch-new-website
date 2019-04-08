from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Coach


def finde_deinen_coach(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/overview.html', {'coaches': coaches})


def coach(request, coach):
    sel_coach = get_object_or_404(Coach, first_name=coach.split('-')[0], name=coach.split('-')[1])
    sport_types = sel_coach.sport_types.all()
    training_methods = sel_coach.training_methods.all()
    return render(request, 'coaches/coach.html', {'coach': sel_coach, 'sport_types': sport_types, 'training_methods': training_methods})


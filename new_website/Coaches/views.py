from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Coach


def finde_deinen_coach(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/overview.html', {'coaches': coaches})


def coach(request, coach):
    sel_coach = get_object_or_404(Coach, first_name=coach.split('-')[0], name=coach.split('-')[1])
    return render(request, 'coaches/coach.html', {'coach': sel_coach})


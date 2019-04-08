from django.shortcuts import render

# Create your views here.
from .models import Coach


def overview(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/overview.html', {'coaches': coaches})

from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Page


def index(request):
    page = get_object_or_404(Page, url="index")
    return render(request, 'website/index.html', {'page': page})

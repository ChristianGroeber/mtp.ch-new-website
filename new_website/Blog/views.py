from django.shortcuts import render

# Create your views here.
from .models import Post


def overview(request):
    post_list = Post.objects.all()
    return render(request, 'Blog/overview.html', {'post_list': post_list})

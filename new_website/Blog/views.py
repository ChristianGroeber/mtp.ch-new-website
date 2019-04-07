from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post, Author


def overview(request):
    post_list = Post.objects.all()
    return render(request, 'Blog/overview.html', {'post_list': post_list})


def blog_post(request, id):
    post = get_object_or_404(Post, id=id)
    author = get_object_or_404(Post, id=id).author
    return render(request, 'Blog/blog_post.html', {'post': post, 'author': author})

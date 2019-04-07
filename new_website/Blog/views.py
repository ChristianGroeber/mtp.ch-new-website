from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Post, Author


def overview(request):
    post_list = Post.objects.filter(publish=True).order_by('-date_posted')
    for post in post_list:
        post.check_if_unpublish()
    return render(request, 'Blog/overview.html', {'post_list': post_list})


def blog_post(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.publish:
        return redirect('blog_overview')
    author = get_object_or_404(Post, id=id).author
    return render(request, 'Blog/blog_post.html', {'post': post, 'author': author})

from .models import Page


def pages(request):
    ret = {'pages': Page.objects.filter(show_on_page=True)}
    return ret

from django.contrib import admin

# Register your models here.
from .models import Post, Author

admin.site.register(Author)
admin.site.register(Post)

import datetime

from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from django.utils import timezone
from froala_editor.fields import FroalaField


class Author(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.CharField(max_length=500, blank=True)
    is_coach = models.BooleanField(default=False)  # TODO connect to Coach Object
    birthday = models.DateField()
    image = models.ImageField(blank=True, upload_to='author_images/')
    about_the_author = FroalaField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.name)


class Post(models.Model):
    author = ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    text = FroalaField()
    main_image = models.ImageField(blank=True, upload_to='post_images/')
    date_posted = models.DateField(default=timezone.now())
    publish = models.BooleanField(default=True)
    date_to_unpublish = models.DateField(blank=True)

    def __str__(self):
        return self.title

    def check_if_unpublish(self):
        print(type(datetime.datetime.now().date()))
        if self.date_to_unpublish < datetime.datetime.now().date():
            self.publish = False

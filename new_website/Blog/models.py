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
    Image = models.ImageField(blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.name)


class Post(models.Model):
    author = ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    text = FroalaField()
    main_image = models.ImageField(blank=True, upload_to='post_images/')
    date_posted = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title

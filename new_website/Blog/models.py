from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from froala_editor.fields import FroalaField


class Author(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.CharField(max_length=500)
    is_coach = models.BooleanField(default=False)  # TODO connect to Coach Object
    birthday = models.DateField()
    Image = models.ImageField()


class Post(models.Model):
    author = ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    text = FroalaField()
    main_image = models.ImageField()

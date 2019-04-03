from django.db import models

# Create your models here.


class Row(models.Model):
    title = models.CharField(max_length=20, blank=True)
    html_id = models.CharField(max_length=10, blank=True)
    text = models.CharField(max_length=1000, blank=True)
    # image = models.ImageField()


class Content(models.Model):
    rows = models.ManyToManyField(Row)


class Page(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    show_on_page = models.BooleanField(default=True)
    content = models.ManyToManyField(Content, blank=True)

    def __str__(self):
        return self.name

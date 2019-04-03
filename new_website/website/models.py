from django.db import models

# Create your models here.


class Page(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

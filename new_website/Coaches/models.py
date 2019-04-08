from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.


class SportType(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class TrainingMethod(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Coach(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='coaches/')
    certificates = FroalaField()
    rating = models.CharField(max_length=1, blank=True)
    sport_types = models.ManyToManyField(SportType)
    training_methods = models.ManyToManyField(TrainingMethod)

    def __str__(self):
        return str(self.first_name) + " " + str(self.name)

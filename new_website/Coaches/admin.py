from django.contrib import admin

# Register your models here.
from .models import SportType, TrainingMethod, Coach

admin.site.register(SportType)
admin.site.register(TrainingMethod)
admin.site.register(Coach)

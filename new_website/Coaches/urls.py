from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.finde_deinen_coach, name='finde_deinen_coach'),
    path('<coach>/', views.coach),
]

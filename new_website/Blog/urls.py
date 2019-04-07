from django.urls import path

from . import views

urlpatterns = [
    path('', views.overview, name='blog_overview'),
    path('<id>/', views.blog_post)
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<id>/', views.blog_post)
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_feed, name='video_feed'),
]

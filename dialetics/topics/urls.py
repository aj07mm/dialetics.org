from django.contrib import admin
from django.urls import include, path
from topics import views

urlpatterns = [
    path('<topic_name>/', views.TopicView.as_view()),
]

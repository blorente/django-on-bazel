from django.urls import path

from notes import views

urlpatterns = [
    path("health/", views.health),
    path("hello/", views.hello),
    path("notes/", views.notes),
]

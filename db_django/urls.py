from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/", views.teacher, name="teacher"),
    path("courses/", views.courses, name="courses")
]

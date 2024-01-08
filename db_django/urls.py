from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/", views.teacher, name="teacher"),
    path("courses/", views.courses, name="courses"),
    path("teacher_courses/<int:teacher_id>", views.teacher_courses, name="teacher_courses")
]

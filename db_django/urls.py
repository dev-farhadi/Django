from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/<int:name_text>", views.teacher, name="teacher")
]

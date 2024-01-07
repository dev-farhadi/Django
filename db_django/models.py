from django.db import models

class Teacher(models.Model):
    name_text = models.CharField(max_length=100)

class Courses(models.Model):
    name_text = models.CharField(max_length=100)

from django.db import models

class Teacher(models.Model):
    name_text = models.CharField(max_length=100)

class Courses(models.Model):
    name_text = models.CharField(max_length=100)

class Teacher_courses(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courses_id = models.ForeignKey(Courses, on_delete=models.CASCADE)

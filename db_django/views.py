from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
from django.template import loader
from .models import Courses
from .models import Teacher_courses

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def teacher(request):
    b = Teacher.objects.all()
    template = loader.get_template("db_django/index.html")
    context = {
         "teachers_list": b,
    }

    return HttpResponse(template.render(context, request))

def courses(request):
    b = Courses.objects.all()
    template = loader.get_template("db_django/courses.html")
    context = {
          "courses_list": b,
    }

    return HttpResponse(template.render(context, request))

def teacher_courses(request, teacher_id):
    
  #teacher_id = 2 # Provide the desired teacher ID

  course_names = Courses.objects.filter(teacher_courses__teacher_id_id=teacher_id).values_list('name_text', flat=True)
  response_str = ', '.join(course_names)

  return HttpResponse(response_str)



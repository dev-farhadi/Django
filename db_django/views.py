from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
from django.template import loader
from .models import Courses

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


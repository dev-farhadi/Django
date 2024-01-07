from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def teacher(request, name_text):
    return HttpResponse("this is teachers name %s."%name_text)

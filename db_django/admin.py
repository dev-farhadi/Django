from django.contrib import admin
from .models import Teacher
from .models import Courses

admin.site.register(Courses)
admin.site.register(Teacher)

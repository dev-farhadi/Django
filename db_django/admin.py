from django.contrib import admin
from .models import Teacher
from .models import Courses
from .models import Teacher_courses

admin.site.register(Teacher_courses)
admin.site.register(Courses)
admin.site.register(Teacher)

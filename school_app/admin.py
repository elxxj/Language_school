from django.contrib import admin
from .models import Language, Course, Level, CourseEdition, Teacher, Student, Enrollment, Review

# Register your models here.

admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Level)
admin.site.register(CourseEdition)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Review)

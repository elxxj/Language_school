from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CourseEdition(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    max_students = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    editions = models.ManyToManyField(CourseEdition)
    bio = models.TextField(null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_edition = models.ForeignKey(CourseEdition, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.name}- {self.course_edition.name}'


class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.student.name} {self.student.surname}'

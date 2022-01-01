from datetime import datetime
from django.db import models
from users.models import Professor, Student
from courses.models import Course


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    grade = models.DecimalField(max_digits=4, decimal_places=2)


class Professor_Assignment(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)
    uploaded_date = models.DateTimeField(default=datetime.now)
    due_date = models.DateTimeField(default=datetime.now)
    task_file = models.FileField(upload_to='assignments/%Y/')
    percentage = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Student_Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(
        Professor_Assignment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    submitted = models.BooleanField(default=False)
    task_file = models.FileField(upload_to='assignments/%Y/', null=True)
    uploaded_date = models.DateTimeField(default=datetime.now)

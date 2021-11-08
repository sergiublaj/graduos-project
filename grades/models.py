from datetime import datetime
from django.db import models
from users.models import Professor, Student
from courses.models import Course

class Grade(models.Model):
<<<<<<< HEAD
   student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
   course_id = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
   grade = models.DecimalField(max_digits = 4, decimal_places = 2)

class Professor_Assignment(models.Model):
   professor_id = models.ForeignKey(Professor, on_delete = models.DO_NOTHING)
   course_id = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
=======
   student = models.ForeignKey(Student, on_delete = models.DO_NOTHING, null = True)
   course = models.ForeignKey(Course, on_delete = models.DO_NOTHING, null = True)
   grade = models.DecimalField(max_digits = 4, decimal_places = 2)

class Professor_Assignment(models.Model):
   professor = models.ForeignKey(Professor, on_delete = models.DO_NOTHING, null = True)
   course = models.ForeignKey(Course, on_delete = models.DO_NOTHING, null = True)
>>>>>>> 87ca4fb (added authenticate functions)
   name = models.CharField(max_length = 128)
   date = models.DateTimeField(default = datetime.now)
   file_uploaded = models.FileField()
   percentage = models.IntegerField(default = 100)
   
class Student_Assignment(models.Model):
<<<<<<< HEAD
   student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
   assignment_id = models.ForeignKey(Professor_Assignment, on_delete = models.CASCADE)
=======
   student = models.ForeignKey(Student, on_delete = models.DO_NOTHING, null = True)
   assignment = models.OneToOneField(Professor_Assignment, on_delete = models.CASCADE, null = True)
>>>>>>> 87ca4fb (added authenticate functions)
   grade = models.DecimalField(max_digits = 4, decimal_places = 2)
   submitted = models.BooleanField(default = False)
   file_uploaded = models.FileField()
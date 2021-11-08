from django.db import models
from users.models import Student, Professor

class Course(models.Model):
   name = models.CharField(max_length = 128)
   year = models.CharField(max_length = 32)
   semester = models.IntegerField()
   description = models.CharField(max_length = 128)
   credits_no = models.IntegerField(default = 4)
<<<<<<< HEAD
   photo = models.ImageField(upload_to = 'photos/courses/%Y/')
   
   def __str__(self):
      return self.name
   
class Student_Course(models.Model):
   student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
   course_id = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
   
class Professor_Course(models.Model):
   professor_id = models.ForeignKey(Professor, on_delete = models.DO_NOTHING)
   course_id = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
=======
   photo = models.ImageField(upload_to = 'photos/courses/%Y/', blank = True)
   students = models.ManyToManyField(Student, related_name = 'coursants')
   professors =  models.ManyToManyField(Professor, related_name = 'instructors')
   
   def __str__(self):
      return self.name
>>>>>>> 87ca4fb (added authenticate functions)

   
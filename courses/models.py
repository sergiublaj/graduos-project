from django.db import models
from users.models import Student, Professor

class Course(models.Model):
   name = models.CharField(max_length = 128)
   year = models.CharField(max_length = 32)
   semester = models.IntegerField()
   description = models.CharField(max_length = 128)
   credits_no = models.IntegerField(default = 4)
   photo = models.ImageField(upload_to = 'photos/courses/%Y/', blank = True)
   students = models.ManyToManyField(Student, related_name = 'coursants')
   professors =  models.ManyToManyField(Professor, related_name = 'instructors')
   
   def __str__(self):
      return self.name

   
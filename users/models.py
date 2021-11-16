from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date

class Person(models.Model):
   user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
   photo = models.ImageField(upload_to = 'photos/persons/%Y/', blank = True)
   phone = models.CharField(max_length = 10)
   registration_date = models.DateTimeField(default = datetime.now, blank = True)
   country = models.CharField(max_length = 64)
   address = models.CharField(max_length = 128)
   birth_date = models.DateField(default = date.today() - timedelta(days = 18 * 365))
   sex = models.CharField(default = 'F', max_length = 1)
  
   def __str__(self):
      return self.user.first_name + " " + self.user.last_name
   
class Student(models.Model):
   person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True)
   identification_no = models.IntegerField()
   university = models.CharField(max_length = 64)
   faculty = models.CharField(max_length = 64)
   study_level = models.CharField(default = "Bachelor", max_length = 64)
   study_year = models.IntegerField(default = 1)
   final_grade = models.DecimalField(max_digits = 4, decimal_places = 2, default = 0, blank = True)
   accumulated_credits = models.IntegerField(default = 0, blank = True)
   outstanding_credits = models.IntegerField(default = 0, blank = True)
   
   def __str__(self):
      return self.person.user.first_name + " " + self.person.user.last_name
   
class Professor(models.Model):
   person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True)
   department = models.CharField(max_length = 128)
   rank = models.CharField(max_length = 128)
   office_address = models.CharField(max_length = 128)
   website = models.URLField(blank = True)
   
   def __str__(self):
      return self.person.user.first_name + " " + self.person.user.last_name 
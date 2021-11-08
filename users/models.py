from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date

class Person(models.Model):
<<<<<<< HEAD
   user_id = models.ForeignKey(User, on_delete = models.CASCADE)
   photo = models.ImageField(upload_to = 'photos/persons/%Y/')
=======
   user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
   photo = models.ImageField(upload_to = 'photos/persons/%Y/', blank = True)
>>>>>>> 87ca4fb (added authenticate functions)
   phone = models.CharField(max_length = 10)
   registration_date = models.DateTimeField(default = datetime.now, blank = True)
   country = models.CharField(max_length = 64)
   address = models.CharField(max_length = 128)
   birth_date = models.DateField(default = date.today() - timedelta(days = 18 * 365))
   sex = models.CharField(default = 'F', max_length = 1)
  
   def __str__(self):
<<<<<<< HEAD
      return self.User.username
   
class Student(models.Model):
   student_id = models.ForeignKey(Person, on_delete = models.CASCADE)
=======
      return self.user.username
   
class Student(models.Model):
   person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True)
>>>>>>> 87ca4fb (added authenticate functions)
   identification_no = models.IntegerField()
   university = models.CharField(max_length = 64)
   faculty = models.CharField(max_length = 64)
   study_level = models.CharField(default = "Bachelor", max_length = 64)
   study_year = models.IntegerField(default = 1)
<<<<<<< HEAD
   final_grade = models.DecimalField(max_digits = 4, decimal_places = 2)
   accumulated_credits = models.IntegerField()
   outstanding_credits = models.IntegerField(default = 0)
   
   def __str__(self):
      return self.Person.User.username
   
class Professor(models.Model):
   professor_id = models.ForeignKey(User, on_delete = models.CASCADE)
   department = models.CharField(max_length = 128)
   rank = models.CharField(max_length = 128)
   office_address = models.CharField(max_length = 128)
   website = models.URLField()
  
   def __str__(self):
      return self.Person.User.username
=======
   final_grade = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True)
   accumulated_credits = models.IntegerField(blank = True)
   outstanding_credits = models.IntegerField(default = 0)
   
   def __str__(self):
      return self.person.user.username
   
class Professor(models.Model):
   person = models.ForeignKey(Person, on_delete = models.CASCADE, null = True)
   department = models.CharField(max_length = 128)
   rank = models.CharField(max_length = 128)
   office_address = models.CharField(max_length = 128)
   website = models.URLField(blank = True)
  
   def __str__(self):
      return self.person.user.username
>>>>>>> 87ca4fb (added authenticate functions)

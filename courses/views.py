from django.shortcuts import render, redirect

from courses.models import Course
from users.models import Person, Professor, Student

def create_course(request):
   if request.method != 'POST':
      return render(request, 'users/dashboard.html')
   
   name = request.POST['name'].capitalize()
   code = request.POST['code']
   year = request.POST['year']
   semester = request.POST['semester']
   credits_no = request.POST['credits_no']
   photo = request.POST['photo']
   description = request.POST['description']
   
   allCourses = Course.objects.all()

   if allCourses.filter(name = name).exists():
      # messages.error(request, 'Course name already taken!')
      return redirect('dashboard')
   
   if allCourses.filter(code = code).exists():
      # messages.error(request, 'Course code already taken!')
      return redirect('dashboard')
   
   course = Course.objects.create(name = name, code = code, year = year, semester = semester, credits_no = credits_no, photo = photo, description = description)

   course.save()
   course.students.set([])
   course.professors.add(Professor.objects.get(person = Person.objects.get(user = request.user)))
   
   return redirect('dashboard')

def join_course(request):
   if request.method != 'POST':
      return render(request, 'users/dashboard.html')
   
   code = request.POST["code"]
   
   allCourses = Course.objects.all()

   if not allCourses.filter(code = code).exists():
      # messages.error(request, 'Course code does not exist!')
      return redirect('dashboard')
   
   student = Student.objects.get(person = Person.objects.get(user = request.user))
   
   if student.courses.filter(code = code).exists():
      # messages.error(request, 'You are already enrolled to that course')
      return redirect('dashboard')
   
   course = Course.objects.get(code = code)
   course.students.add(student)
   course.save()
   
   return redirect('dashboard')
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from users.models import Person, Student, Professor
from courses.models import Course

def register(request):
   if request.method != 'POST':
      return render(request, 'users/register.html')
   
   user = register_user(request)
   
   # person = register_person(request, user)
   
   # is_student = request.POST['is_student']
   # if is_student == True:
   #    register_student(request, person)
   # else:
   #    register_professor(request, person)   
      
   messages.success(request, 'Successfully registered!')
   return redirect('login')
   
   
def register_user(request):
   first_name = request.POST['first_name'].capitalize()
   last_name = request.POST['last_name'].capitalize()
   username = request.POST['username']
   email = request.POST['email']
   password = request.POST['password']
   password2 = request.POST['password2']
   
   allUsers = User.objects
   
   if password != password2:
      messages.error(request, 'Passwords do not match!')
      return redirect('register')

   if allUsers.filter(username = username).exists():
      messages.error(request, 'Username already taken!')
      return redirect('register')
   
   if allUsers.filter(email = email).exists():
      messages.error(request, 'Email already taken!')
      return redirect('register')      
   
   user = User.objects.create(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
   user.save()
   
   return user

def register_person(request, user):   
   photo = request.POST['photo']
   phone = request.POST['phone']
   country = request.POST['country']
   address = request.POST['address']
   birth_date = request.POST['birth_date']
   sex = request.POST['sex']
   
   print(user)
   
   person = Person.objects.create(user = user, photo = photo, phone = phone, country = country, address = address, birth_date = birth_date, sex = sex)
   person.save()
   
   return person

def register_student(request, person):   
   identification_no = request.POST['identification_no']
   university = request.POST['university']
   faculty = request.POST['faculty']
   study_level = request.POST['study_level']
   study_year = request.POST['study_year']
   final_grade = request.POST['final_grade']
   
   student = Student.objects.create(person = person, identification_no = identification_no, university = university, faculty = faculty, study_level = study_level, study_year = study_year, final_grade = final_grade)
   student.save()

def register_professor(request, person):
   department = request.POST['department']
   rank = request.POST['rank']
   office_address = request.POST['office_address']
   website = request.POST['website']
   
   professor = Professor.objects.create(person = person, department = department, rank = rank, office_address = office_address, website = website)
   professor.save()
   
def login(request):
   if request.method != 'POST':
      return render(request, 'users/login.html')
   
   username = request.POST['username']
   password = request.POST['password']
   
   user = auth.authenticate(username = username, password = password)
   
   if user is None:
      messages.error(request, 'Invalid credentials!')
      return redirect('login')
   
   auth.login(request, user)
   messages.success(request, 'You are now logged in!')
   return redirect('dashboard')

def logout(request):
   if request.method == "POST":
      auth.logout(request)
      messages.success(request, 'You are now logged out.')
      return redirect('index')

def dashboard(request):
   person = Person.objects.filter(user = request.user)
   student = Student.objects.filter(person = person)
   professor = Professor.objects.filter(person = person)
   
   courses = None
   if student is None:
      courses = Course.objects.filter(professors = professor)
   else:
      courses = Course.objects.filter(students = student)
      
   context = {
      'courses': courses
   }
   
   return render(request, 'users/dashboard.html', context)



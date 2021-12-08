from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from users.models import Person, Student, Professor


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method != 'POST':
        return render(request, 'users/register.html')

    register_user(request)

    register_person(request)

    is_student = request.POST['is_student']

    if is_student == 'True':
        register_student(request)
    else:
        register_professor(request)

    messages.success(request, 'Successfully registered! You can now log in.')
    return redirect('login')


def register_user(request):
    first_name = request.POST['first_name'].capitalize()
    last_name = request.POST['last_name'].capitalize()
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    allUsers = User.objects.all()

    if allUsers.filter(username=username).exists():
        messages.error(request, 'Username already taken!')
        return render(request, 'users/register.html')

    if allUsers.filter(email=email).exists():
        messages.error(request, 'Email already taken!')
        return render(request, 'users/register.html')

    if password != password2:
        messages.error(request, 'Passwords do not match!')
        return render(request, 'users/register.html')

    user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                    username=username, email=email)
    user.set_password(password)

    user.save()


def register_person(request):
    user = User.objects.get(username=request.POST['username'])
    photo = request.FILES['photo']
    phone = request.POST['phone']
    country = request.POST['country']
    address = request.POST['address']
    birth_date = request.POST['birth_date']
    gender = request.POST['gender']

    person = Person.objects.create(user=user, photo=photo, phone=phone,
                                   country=country, address=address, birth_date=birth_date, gender=gender)
    person.save()


def register_student(request):
    person = Person.objects.get(user=User.objects.get(
        username=request.POST['username']))
    identification_no = request.POST['identification_no']
    university = request.POST['university']
    faculty = request.POST['faculty']
    study_level = request.POST['study_level']
    study_year = request.POST['study_year']

    student = Student.objects.create(person=person, identification_no=identification_no,
                                     university=university, faculty=faculty, study_level=study_level, study_year=study_year)
    student.save()


def register_professor(request):
    person = Person.objects.get(user=User.objects.get(
        username=request.POST['username']))
    department = request.POST['department']
    rank = request.POST['rank']
    office_address = request.POST['office_address']
    website = request.POST['website']

    professor = Professor.objects.create(
        person=person, department=department, rank=rank, office_address=office_address, website=website)
    professor.save()


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method != 'POST':
        return render(request, 'users/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is None:
        messages.error(request, 'Invalid credentials!')
        return redirect('login')

    auth.login(request, user)

    return redirect('dashboard')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('login')


def dashboard(request):
    try:
        person = Person.objects.get(user=request.user)
    except:
        return redirect('index')

    try:
        professor = Professor.objects.get(person=person)
        courses = professor.courses.all()
        is_student = False
    except:
        student = Student.objects.get(person=person)
        courses = student.courses.all()
        is_student = True

    context = {
        'courses': courses,
        'is_student': is_student
    }

    return render(request, 'users/dashboard.html', context)

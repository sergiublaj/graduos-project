from django.contrib import messages, auth
from django.shortcuts import redirect, render

from grades.models import Grade
from invitations.models import Invitation
from notifications.models import Notification
from notifications.views import create_notification
from users.models import Person, Student, Professor
from users.user_builder import UserBuilder


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method != 'POST':
        return render(request, 'users/register.html')

    user_builder = UserBuilder(request)

    user_builder.register_account()

    messages.success(request, 'Successfully registered! You can now log in.')

    return redirect('login')


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
    if request.method != 'POST':
        return redirect('index')

    auth.logout(request)

    messages.success(request, 'You are now logged out.')

    return redirect('login')


def dashboard(request):
    try:
        person = Person.objects.get(user=request.user)
    except:
        return redirect('index')

    try:
        student = Student.objects.get(person=person)
        courses = student.courses.all()
        is_student = True
    except:
        professor = Professor.objects.get(person=person)
        courses = professor.courses.all()
        is_student = False

    try:
        invitations = Invitation.objects.filter(to_user=request.user).filter(closed=False)
    except:
        invitations = None

    context = {
        'courses': courses,
        'invitations': invitations,
        'is_student': is_student
    }

    return render(request, 'users/dashboard.html', context)


def profile(request):
    try:
        person = Person.objects.get(user=request.user)
    except:
        return redirect('index')

    try:
        student = Student.objects.get(person=person)
        grades = Grade.objects.filter(student=student)
        is_student = True
        professor = None
    except:
        professor = Professor.objects.get(person=person)
        is_student = False
        student = None
        grades = None

    context = {
        'is_student': is_student,
        'person': person,
        'student': student,
        'professor': professor,
        'grades': grades
    }

    return render(request, 'users/profile.html', context)


def edit_profile(request):
    if request.method != 'POST':
        return redirect('profile')

    if not request.user.is_authenticated:
        return redirect('index')

    photo = request.FILES.get('inputPhoto', None)
    username = request.POST['inputUsername']
    email = request.POST['inputEmail']
    phone = request.POST['inputPhone']
    country = request.POST['inputCountry']
    address = request.POST['inputAddress']

    user = request.user
    user.username = username
    user.email = email
    user.save()

    person = Person.objects.get(user=request.user)
    person.photo = photo if photo != None else person.photo
    person.phone = phone
    person.address = address
    person.country = country
    person.save()

    notification = get_profile_edit_notification(request)

    return create_notification(request, 'profile', notification)


def get_profile_edit_notification(request):
    messages.success(request, f'Successfully changed your profile.')

    title = 'Profile changes'
    description = ('\n').join(('Congratulations!',
                               'You have successfully changed your personal information.',
                               'Navigate to dashboard/profile and see your information.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification

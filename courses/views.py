from django.shortcuts import redirect
from django.contrib import messages

from courses.models import Course
from notifications.views import create_notification
from users.models import Person, Professor, Student
from notifications.models import Notification


def create_course(request):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        professor = Professor.objects.get(
            person=Person.objects.get(user=request.user))
    except:
        return redirect('dashboard')

    name = request.POST['name'].capitalize()
    code = request.POST['code']
    year = request.POST['year']
    semester = request.POST['semester']
    credits_no = request.POST['credits_no']
    photo = request.FILES['photo']
    description = request.POST['description']

    allCourses = Course.objects.all()

    if allCourses.filter(name=name).exists():
        messages.error(request, 'Course name already taken!')
        return redirect('dashboard')

    if allCourses.filter(code=code).exists():
        messages.error(request, 'Course code already taken!')
        return redirect('dashboard')

    course = Course.objects.create(name=name, code=code, year=year, semester=semester,
                                   credits_no=credits_no, photo=photo, description=description)

    course.save()
    course.students.set([])
    course.professors.add(professor)

    notification = get_create_course_notification(request, name, code)

    return create_notification(request, 'dashboard', notification)


def get_create_course_notification(request, name, code):
    messages.success(request, f'Successfully created course {name}.')

    title = 'New course created'
    description = ('\n').join(('Congratulations!',
                              f'You have successfully created course {name}.',
                               f'Share the code {code} to your students.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def join_course(request):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        student = Student.objects.get(
            person=Person.objects.get(user=request.user))
    except:
        return redirect('dashboard')

    code = request.POST['code']

    allCourses = Course.objects.all()

    if not allCourses.filter(code=code).exists():
        messages.error(request, 'Course code does not exist!')
        return redirect('dashboard')

    if student.courses.filter(code=code).exists():
        messages.error(request, 'You are already enrolled to that course')
        return redirect('dashboard')

    course = Course.objects.get(code=code)
    course.students.add(student)
    course.save()

    notification = get_join_course_notification(request, course.name)

    return create_notification(request, 'dashboard', notification)


def get_join_course_notification(request, name):
    messages.success(request, f'Successfully joined course {name}.')

    title = 'Joined a new course'
    description = ('\n').join(('Congratulations!',
                              f'You have successfully joined course {name}.',
                               'Do your assignments and get the highest grade.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def leave_course(request, fake_course_id):
    if request.method != 'POST':
        return redirect('dashboard')

    course_id = fake_course_id if fake_course_id != 0 else request.POST['course_id']

    try:
        student = Student.objects.get(
            person=Person.objects.get(user=request.user))
        course = Course.objects.get(id=course_id)
    except:
        return redirect('dashboard')

    if course not in student.courses.all():
        return redirect('dashboard')

    Course.objects.get(id=course_id).students.remove(student)

    notification = get_leave_course_notification(request, course.name)

    return create_notification(request, 'dashboard', notification)


def get_leave_course_notification(request, name):
    messages.success(request, f'Left course {name}.')

    title = 'Left a course'
    description = ('\n').join((f'You have successfully left course {name}.',
                              'Hope to see you soon!',
                               'All the best!'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def delete_course(request, fake_course_id):
    if request.method != 'POST':
        return redirect('dashboard')

    course_id = fake_course_id if fake_course_id != 0 else request.POST['course_id']

    try:
        professor = Professor.objects.get(
            person=Person.objects.get(user=request.user))
        course = Course.objects.get(id=course_id)
    except:
        return redirect('dashboard')

    if course not in professor.courses.all():
        return redirect('dashboard')

    Course.objects.get(id=course_id).delete()

    notification = get_delete_course_notification(request, course.name)

    return create_notification(request, 'dashboard', notification)


def get_delete_course_notification(request, name):
    messages.success(request, f'Deleted course {name}.')

    title = 'Deleted a course'
    description = ('\n').join((f'You have successfully deleted course {name}.',
                              'Hope you create a new one soon.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification

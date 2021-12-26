from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from courses.models import Course
from grades.models import Professor_Assignment, Student_Assignment
from notifications.views import create_notification
from users.models import Person, Professor, Student
from notifications.models import Notification
from files.models import File


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


def view_course(request, course_id):
    if request.method != 'GET':
        return redirect('dashboard')

    try:
        course = Course.objects.get(id=course_id)
        professor_users = [
            professor.person.user for professor in course.professors.all()]
        student_users = [
            student.person.user for student in course.students.all()]
        course_files = File.objects.filter(course=course)
        professor_assignments = Professor_Assignment.objects.filter(course=course)
        student_assignments = []
        for assignment in professor_assignments:
            student_assignments += Student_Assignment.objects.filter(assignment=assignment)

    except:
        return redirect('dashboard')

    if request.user not in professor_users and request.user not in student_users:
        messages.error(request, 'You do not have permission to view that course!')
        
        return redirect('dashboard')

    context = {
        'course': course,
        'professor_users': professor_users,
        'course_files': course_files,
        'professor_assignments': professor_assignments,
        'student_assignments': student_assignments
    }

    return render(request, 'courses/course.html', context)


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


def kick_participant(request):
    if request.method != 'POST':
        return redirect('dashboard')

    course_id = request.POST['course_id']
    student_id = request.POST['participant_id']

    try:
        course = Course.objects.get(id=course_id)
        professor = Professor.objects.get(
            person=Person.objects.get(user=request.user))
        student = Student.objects.get(
            person=Person.objects.get(user=User.objects.get(id=student_id)))
    except:
        return redirect('dashboard')

    if course not in professor.courses.all():
        messages(request, 'You do not have that permission!')
        return redirect('dashboard')

    if course not in student.courses.all():
        return redirect('dashboard')

    course.students.remove(student)

    student_notification = get_kick_student_notification(
        course.name, professor.person.user, student.person.user)
    student_notification.save()

    professor_notification = get_kick_professor_notification(
        course.name, professor.person.user, student.person.user)
    professor_notification.save()

    return redirect('view_course', course_id=course.id)


def get_kick_student_notification(name, professor, student):
    title = 'Kicked from course'
    description = ('\n').join((f'You have been from course {name} by {professor.last_name} {professor.first_name}.',
                              'You can message him to let him know the reason.',
                               'All the best!'))

    notification = Notification.objects.create(
        user=student, title=title, description=description)

    return notification


def get_kick_professor_notification(name, professor, student):
    title = 'Kicked student from course'
    description = ('\n').join((f'You have successfully kicked {student.last_name} {student.first_name} from course {name}.',
                              'You can message him to let him know the reason.',
                               'All the best!'))

    notification = Notification.objects.create(
        user=professor, title=title, description=description)

    return notification


def leave_course(request):
    if request.method != 'POST':
        return redirect('dashboard')

    course_id = request.POST['course_id']

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


def delete_course(request):
    if request.method != 'POST':
        return redirect('dashboard')

    course_id = request.POST['course_id']

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

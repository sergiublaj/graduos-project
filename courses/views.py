from django.shortcuts import render, redirect
from django.contrib import messages

from courses.models import Course
from users.models import Person, Professor, Student


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

    return redirect('dashboard')


def join_course(request):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        student = Student.objects.get(
            person=Person.objects.get(user=request.user))
    except:
        return redirect('dashboard')

    code = request.POST["code"]

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

    messages.success(request, f'Successfully joined course {course.name}.')

    return redirect('dashboard')


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

    print(Course.objects.get(id=course_id))

    Course.objects.get(id=course_id).students.remove(student)

    messages.success(request, f'Left course {course.name}.')

    return redirect('dashboard')


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

    print(Course.objects.get(id=course_id))

    Course.objects.get(id=course_id).delete()

    messages.success(request, f'Deleted course {course.name}.')

    return redirect('dashboard')

import os
import mimetypes

from django.shortcuts import redirect, HttpResponse

from courses.models import Course
from grades.models import Grade, Professor_Assignment, Student_Assignment
from users.models import Person, Professor, Student
from notifications.models import Notification


def add_assignment(request, course_id):
    if request.method != 'POST':
        return redirect('dashboard')

    name = request.POST['assignment_name']
    content = request.FILES['assignment_content']
    due = request.POST['assignment_due']
    percentage = int(request.POST['assignment_percentage'])

    try:
        course = Course.objects.get(id=course_id)
        professor = Professor.objects.get(
            person=Person.objects.get(user=request.user))
        assignments = Professor_Assignment.objects.filter(course=course)
    except:
        return redirect('dashboard')

    if course not in professor.courses.all():
        return redirect('view_course', course_id=course.id)

    total_percentage = percentage + \
        sum([assignment.percentage for assignment in assignments])
    if total_percentage > 100:
        return redirect('view_course', course_id=course.id)

    assignment = Professor_Assignment.objects.create(
        professor=professor, course=course, name=name, due_date=due, task_file=content, percentage=percentage)
    assignment.save()

    try:
        students = course.students.all()

        for student in students:
            student_assignment = Student_Assignment.objects.create(
                student=student, assignment=assignment)
            student_assignment.save()

            notification = get_add_professor_assignment_student_notification(
                student.person.user, course.name, assignment)
            notification.save()
    except:
        pass

    notification = get_add_professor_assignment_professor_notification(
        request, course.name, assignment)
    notification.save()

    return redirect('view_course', course_id=course.id)


def get_add_professor_assignment_professor_notification(request, name, assignment):
    title = 'Assignment added'
    description = ('\n').join(
        (f'You have sucessfully added assignment {assignment.name} to course {name}. ',
         f'Due date: {assignment.due_date}.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def get_add_professor_assignment_student_notification(student, name, assignment):
    title = 'New assignment'
    description = ('\n').join(
        (f'You have a new assignment: {assignment.name} at course {name}. ',
         f'Due date: {assignment.due_date}.'))

    notification = Notification.objects.create(
        user=student, title=title, description=description)

    return notification


def download_assignment(request, course_id, assignment_id):
    if request.method != 'GET':
        return redirect('dashboard')

    course = Course.objects.get(id=course_id)
    assignment = Professor_Assignment.objects.get(id=assignment_id)

    if assignment.course != course:
        return redirect('dashboard')

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filepath = BASE_DIR + '/media/' + str(assignment.task_file)

    path = open(filepath, 'rb')

    mime_type, _ = mimetypes.guess_type(filepath)

    response = HttpResponse(path, content_type=mime_type)

    response['Content-Disposition'] = "attachment; filename=%s" % \
        (assignment.name + '.' + filepath.split('.')[-1])

    return response


def delete_assignment(request):
    if request.method != 'POST':
        return redirect('dashboard')

    course_id = request.POST['course_id']
    assignment_id = request.POST['assignment_id']
    try:
        course = Course.objects.get(id=course_id)
        assignment = Professor_Assignment.objects.get(id=assignment_id)
    except:
        return redirect('dashboard')

    if assignment.course != course:
        return redirect('dashboard')

    assignment.delete()

    notification = get_delete_assignment_notification(
        request, course.name, assignment.name)
    notification.save()

    return redirect('view_course', course_id=course_id)


def get_delete_assignment_notification(request, course_name, assignment_name):
    title = 'Assignment deleted'
    description = ('\n').join(
        (f'You have sucessfully deleted assignment {assignment_name} from course {course_name}. ', ''))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def add_submission(request, course_id, assignment_id, submission_id):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        course = Course.objects.get(id=course_id)
        student = Student.objects.get(
            person=Person.objects.get(user=request.user))
        assignment = Professor_Assignment.objects.get(id=assignment_id)
        submission = Student_Assignment.objects.get(id=submission_id)
    except:
        return redirect('dashboard')

    if student not in course.students.all():
        return redirect('dashboard')

    if course != assignment.course:
        return redirect('dashboard')

    if submission.assignment != assignment:
        return redirect('dashboard')

    submission.submitted = True
    submission.task_file = request.FILES['submission_content']
    submission.save()

    notification = get_add_submission_notification(
        request, course.name, submission)
    notification.save()

    return redirect('view_course', course_id=course.id)


def get_add_submission_notification(request, course_name, submission):
    title = 'Submission sent'
    description = ('\n').join(
        (f'You have sucessfully submited your work for assignment {submission.assignment.name} from course {course_name}. ', ''))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def download_submission(request, course_id, assignment_id, submission_id):
    if request.method != 'GET':
        return redirect('dashboard')

    try:
        course = Course.objects.get(id=course_id)
        assignment = Professor_Assignment.objects.get(id=assignment_id)
        submission = Student_Assignment.objects.get(id=submission_id)
    except:
        return redirect('dashboard')

    if submission.assignment != assignment:
        return redirect('dashboard')

    if submission.assignment.course != course:
        return redirect('dashboard')

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filepath = BASE_DIR + '/media/' + str(submission.task_file)

    path = open(filepath, 'rb')

    mime_type, _ = mimetypes.guess_type(filepath)

    response = HttpResponse(path, content_type=mime_type)

    response['Content-Disposition'] = "attachment; filename=%s" % \
        (submission.student.person.user.first_name + submission.student.person.user.last_name +
            '-' + assignment.name + '.' + filepath.split('.')[-1])

    return response


def grade_submission(request, course_id, assignment_id, submission_id):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        course = Course.objects.get(id=course_id)
        assignment = Professor_Assignment.objects.get(id=assignment_id)
        submission = Student_Assignment.objects.get(id=submission_id)
    except:
        return redirect('dashboard')

    if submission.assignment != assignment:
        return redirect('dashboard')

    if submission.assignment.course != course:
        return redirect('dashboard')

    grade_value = request.POST['grade_value']

    submission.grade = grade_value
    submission.save()
    
    mark = 0
    try:
        student_assignments = Student_Assignment.objects.filter(student = submission.student).get(course = course)
        
        for student_assignment in student_assignments:
            mark += student_assignment.grade * student_assignment.assignment.percentage / 100
    except:
        pass
    
    try:
        grade = Grade.objects.filter(student = submission.student).get(course = course)
        grade.grade = mark
        grade.save()
    except:
        grade = Grade.objects.create(student = submission.student, course = course, grade = mark)
        grade.save()
    
    professor_notification = get_grade_submission_professor_notification(request.user, submission.student.person.user, course.name, submission)
    professor_notification.save()
    
    student_notification = get_grade_submission_student_notification( request.user, submission.student.person.user, course.name, submission)
    student_notification.save()
    
    return redirect('view_course', course_id=course.id)

def get_grade_submission_professor_notification(professor, student, course_name, submission):
    title = 'Assignment graded'
    description = ('\n').join(
        (f'You have sucessfully graded {student.last_name} {student.first_name} with {submission.grade}/10.',
         f'Course: {course_name}, assignment name: {submission.assignment.name}.'))

    notification = Notification.objects.create(
        user=professor, title=title, description=description)

    return notification

def get_grade_submission_student_notification(professor, student, course_name, submission):
    title = 'Assignment graded'
    description = ('\n').join(
        (f'You have been graded by {professor.last_name} {professor.first_name} with {submission.grade}/10.',
         f'Course: {course_name}, assignment name: {submission.assignment.name}.'))

    notification = Notification.objects.create(
        user=student, title=title, description=description)

    return notification

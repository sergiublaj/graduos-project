import os
import mimetypes

from django.shortcuts import redirect, HttpResponse
from django.contrib import messages

from courses.models import Course
from users.models import Person, Professor
from notifications.models import Notification
from files.models import File

def add_file(request, course_id):
    if request.method != 'POST':
        return redirect('dashboard')

    filename = request.POST['filename']
    filecontent = request.FILES['filecontent']

    try:
        course = Course.objects.get(id=course_id)
        professor = Professor.objects.get(
            person=Person.objects.get(user=request.user))
    except:
        return redirect('dashboard')

    if course not in professor.courses.all():
        messages(request, 'You do not have that permission!')
        return redirect('view_course', course_id=course.id)
 
    new_file = File.objects.create(filename = filename, filecontent = filecontent, course = course)
    new_file.save()

    notification = get_add_file_notification(request, course.name, new_file)
    notification.save()

    return redirect('view_course', course_id=course.id)


def get_add_file_notification(request, name, new_file):
    title = 'File added'
    description = ('\n').join(
        (f'You have sucessfully added file {new_file.filename} to course {name}. ',
        f'File size: {new_file.filecontent.size} kB.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def download_file(request, course_id, file_id):
    if request.method != 'GET':
        return redirect('dashboard')
    
    the_file = File.objects.get(id = file_id)
    the_course = Course.objects.get(id = course_id)
    
    if the_file.course != the_course:
        return redirect('dashboard')
    
    print(the_file.filecontent)
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    filepath = BASE_DIR + '/media/' + str(the_file.filecontent)
    
    path = open(filepath, 'rb')
    
    mime_type, _ = mimetypes.guess_type(filepath)
    
    response = HttpResponse(path, content_type=mime_type)
    
    response['Content-Disposition'] = "attachment; filename=%s" % \
        (the_file.filename + '.' + filepath.split('.')[-1])
    
    return response


def delete_file(request):
    if request.method != 'POST':
        return redirect('dashboard')

    print(request.POST)

    course_id = request.POST['course_id']
    file_id = request.POST['file_id']

    try:
        the_course = Course.objects.get(id = course_id)
        the_file = File.objects.get(id = file_id)
    except:
        return redirect('dashboard')

    if the_file.course != the_course:
        return redirect('dashboard')
 
    the_file.delete()

    notification = get_delete_file_notification(request, the_course.name, the_file)
    notification.save()

    return redirect('view_course', course_id=course_id)


def get_delete_file_notification(request, course_name, file_name):
    title = 'File deleted'
    description = ('\n').join(
        (f'You have sucessfully deleted file {file_name} from course {course_name}. ',
        f'File was {file_name.filecontent.size} kB large.'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification
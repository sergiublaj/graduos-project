from django.contrib import messages
from django.shortcuts import render, redirect

from courses.models import Course
from forum.models import Post
from users.models import Person



def view_messages(request, course_id):
    if request.method != 'GET':
        return redirect('dashboard')


    course = Course.objects.get(id=course_id)
    posts = Post.objects.filter(course_id = course.id).order_by('timestamp')

    context = {
        'course': course,
        'posts': posts
    }

    return render(request, "forum/forum.html", context)



def send_message(request, course_id):
    if request.method != 'POST':
        return redirect('view_messages',course_id=course_id)

    try:
        user = request.user
        content = request.POST['content']
        image = request.user.person.photo
        post = Post.objects.create(author=user, post_content=content, course_id=course_id, image=image)
        post.save()
    except:
        print("Exception")
        pass

    return redirect('view_messages', course_id=course_id)



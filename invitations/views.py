from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

from courses.models import Course
from invitations.models import Invitation
from notifications.models import Notification
from notifications.views import create_notification
from users.models import Person, Professor, Student


def invite_participant(request, course_id):
    if request.method != 'POST':
        return redirect('dashboard')

    email = request.POST['email']

    try:
        course = Course.objects.get(id=course_id)
        participant = User.objects.get(email=email)
        student = Student.objects.get(
            person=Person.objects.get(user=participant))
        professor = None
    except:
        try:
            professor = Professor.objects.get(
                person=Person.objects.get(user=participant))
            student = None
        except:
            notification = get_invalid_notification(
                request, course.name, email)
            notification.save()

            return redirect('view_course', course_id=course_id)

    if len(Invitation.objects.filter(to_user=participant).filter(course=course).filter(closed=False)) > 0:
        notification = get_error_notification(
            request, course.name, participant)
        notification.save()

        return redirect('view_course', course_id=course_id)

    if professor is None and course in student.courses.all():
        notification = get_already_enrolled_notification(
            request, course.name, participant)
        notification.save()

        return redirect('view_course', course_id=course_id)

    if student is None and course in professor.courses.all():
        notification = get_already_enrolled_notification(
            request, course.name, participant)
        notification.save()

        return redirect('view_course', course_id=course_id)

    invitation = Invitation.objects.create(
        course=course, from_user=request.user, to_user=participant)
    invitation.save()

    from_notification = get_from_user_notification(
        course.name, request.user, participant)
    from_notification.save()

    to_notification = get_to_user_notification(
        course.name, request.user, participant)
    to_notification.save()

    return redirect('view_course', course_id=course.id)


def get_invalid_notification(request, course, email):
    title = 'Invitation error'
    description = ('\n').join(
        (f'Cannot invite {email} to join {course}.', 'Are you sure that is a valid email?'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def get_error_notification(request, course, email):
    title = 'Invitation error'
    description = ('\n').join(
        (f'Cannot invite {email} to join {course}.', 'That user needs to accept its ongoing invitation first!'))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def get_already_enrolled_notification(request, course, user):
    title = 'Already enrolled'
    description = ('\n').join(
        (f'{user.last_name} {user.first_name} is already enrolled to {course}.', ''))

    notification = Notification.objects.create(
        user=request.user, title=title, description=description)

    return notification


def get_from_user_notification(course, from_user, to_user):
    person = Person.objects.get(user=to_user)
    pronoun = 'he' if person.gender == 'M' else 'she'

    title = 'Invitation sent'
    description = ('\n').join((f'You have successfully invited {to_user.last_name} {to_user.first_name} to join course {course}.',
                               f'Hope {pronoun} accepts the invitation.'))

    notification = Notification.objects.create(
        user=from_user, title=title, description=description)

    return notification


def get_to_user_notification(course, from_user, to_user):
    title = 'Invitation received'
    description = ('\n').join((f'You have been invited to join course {course} by {from_user.last_name} {from_user.first_name}.',
                               'Hope to see in the class!'))

    notification = Notification.objects.create(
        user=to_user, title=title, description=description)

    return notification


def accept_invitation(request, invitation_id):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        invitation = Invitation.objects.get(id=invitation_id)
    except:
        return redirect('dashboard')

    course = invitation.course
    person = Person.objects.get(user=request.user)

    try:
        student = Student.objects.get(person=person)
        course.students.add(student)
    except:
        professor = Professor.objects.get(person=person)
        course.professors.add(professor)

    invitation.accepted = True
    invitation.closed = True
    invitation.save()

    messages.success(request, 'Successfully accepted the invitation!')

    from_user_notification = get_from_user_accept_notification(
        course.name, invitation.from_user, invitation.to_user)
    from_user_notification.save()

    get_to_user_notification = get_to_user_accept_notification(
        course.name, invitation.from_user, invitation.to_user)

    return create_notification(request, 'dashboard', get_to_user_notification)


def get_from_user_accept_notification(course, from_user, to_user):
    title = 'Invitation accepted'
    description = ('\n').join((f'{to_user.last_name} {to_user.first_name} accepted your invitation to join course {course}.',
                               f'All the best!'))

    notification = Notification.objects.create(
        user=from_user, title=title, description=description)

    return notification


def get_to_user_accept_notification(course, from_user, to_user):
    title = 'Invitation accepted'
    description = ('\n').join((f'You have sucessfully accepted {from_user.last_name} {from_user.first_name}\'s invitation to join course {course}.',
                               'All the best!'))

    notification = Notification.objects.create(
        user=to_user, title=title, description=description)

    return notification


def decline_invitation(request, invitation_id):
    if request.method != 'POST':
        return redirect('dashboard')

    try:
        invitation = Invitation.objects.get(id=invitation_id)
    except:
        return redirect('dashboard')

    invitation.accepted = False
    invitation.closed = True
    invitation.save()

    messages.error(request, 'Declined the invitation.')

    from_user_notification = get_from_user_decline_notification(
        invitation.course.name, invitation.from_user, invitation.to_user)
    from_user_notification.save()

    get_to_user_notification = get_to_user_decline_notification(
        invitation.course.name, invitation.from_user, invitation.to_user)

    return create_notification(request, 'dashboard', get_to_user_notification)


def get_from_user_decline_notification(course, from_user, to_user):
    title = 'Invitation declined'
    description = ('\n').join((f'{to_user.last_name} {to_user.first_name} declined your invitation to join course {course}.',
                               f'All the best!'))

    notification = Notification.objects.create(
        user=from_user, title=title, description=description)

    return notification


def get_to_user_decline_notification(course, from_user, to_user):
    title = 'Invitation declined'
    description = ('\n').join((f'You have declined {from_user.last_name} {from_user.first_name}\'s invitation to join course {course}.',
                               'All the best!'))

    notification = Notification.objects.create(
        user=to_user, title=title, description=description)

    return notification

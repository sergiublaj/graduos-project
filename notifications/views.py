from django.shortcuts import render, redirect

from notifications.models import Notification


def create_notification(request, http_redirect, notification):
    if request.method != 'POST':
        return redirect('index')

    notification.save()

    return redirect(http_redirect)


def view_notifications(request):
    if request.method != 'POST':
        return redirect('dashboard')

    notifications = Notification.objects.filter(
        user=request.user).order_by('-date')

    context = {
        'notifications': notifications
    }

    return render(request, 'notifications/notifications.html', context)


def read_notification(request, notification_id):
    if request.method != 'POST':
        return redirect('view_notifications')

    try:
        notification = Notification.objects.get(id=notification_id)

        if notification.user != request.user:
            return redirect('view_notifications')

        notification.unread = False
        notification.save()
    except:
        pass

    return redirect('view_notifications')


def delete_notification(request, notification_id):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method != 'POST':
        return redirect('dashboard')

    try:
        notification = Notification.objects.get(id=notification_id)

        if notification.user != request.user:
            return redirect('view_notifications')

        notification.delete()
    except:
        pass

    return redirect('view_notifications')

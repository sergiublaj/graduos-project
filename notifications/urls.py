from django.urls import path
from . import views

urlpatterns = [
    path('create_notification', views.create_notification,
         name='create_notification'),
    path('view_notifications', views.view_notifications, name='view_notifications'),
    path('read_notification/<int:notification_id>',
         views.read_notification, name='read_notification'),
    path('delete_notification/<int:notification_id>',
         views.delete_notification, name='delete_notification'),
]

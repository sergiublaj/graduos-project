from django.urls import path
from . import views

urlpatterns = [
    path('create_course', views.create_course, name='create_course'),
    path('view_course/<int:course_id>', views.view_course, name='view_course'),
    path('join_course', views.join_course, name='join_course'),
    path('kick_participant', views.kick_participant, name='kick_participant'),
    path('leave_course', views.leave_course, name='leave_course'),
    path('delete_course', views.delete_course, name='delete_course'),
]

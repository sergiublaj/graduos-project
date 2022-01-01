from django.urls import path
from . import views

urlpatterns = [

    path('view_messages/<int:course_id>', views.view_messages, name='view_messages'),
    path('send_message/<int:course_id>', views.send_message, name='send_message'),
]
from django.urls import path
from . import views

urlpatterns = [
   path('create_course', views.create_course, name = 'create_course'),
   path('delete_course/<int:course_id>', views.delete_course, name = 'delete_course'),
   path('join_course', views.join_course, name = 'join_course'),
]
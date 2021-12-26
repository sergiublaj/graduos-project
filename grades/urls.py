from django.urls import path
from . import views

urlpatterns = [
    path('add_assignment/<int:course_id>',
         views.add_assignment, name='add_assignment'),
    path('download_assignment/<int:course_id>/<int:assignment_id>',
         views.download_assignment, name='download_assignment'),
    path('delete_assignment/',
         views.delete_assignment, name='delete_assignment'),
    
    path('add_submission/<int:course_id>/<int:assignment_id>/<int:submission_id>',
         views.add_submission, name='add_submission'),
    path('download_submission/<int:course_id>/<int:assignment_id>/<int:submission_id>',
         views.download_submission, name='download_submission'),
    path('grade_submission/<int:course_id>/<int:assignment_id>/<int:submission_id>',
         views.grade_submission, name='grade_submission'),
]

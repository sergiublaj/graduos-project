from django.urls import path
from . import views

urlpatterns = [
    path('add_file/<int:course_id>',
         views.add_file, name='add_file'),
    path('download_file/<int:course_id>/<int:file_id>',
         views.download_file, name='download_file'),
    path('delete_file',
         views.delete_file, name='delete_file'),
]

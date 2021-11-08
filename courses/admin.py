from django.contrib import admin
from courses.models import Course

class CourseAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'year', 'semester', 'description' , 'credits_no', 'photo')
  list_display_links = ('id', 'name')
  search_fields = ('id', 'name', 'credits_no', 'semester', 'year')
  list_per_page = 25
  
admin.site.register(Course, CourseAdmin)

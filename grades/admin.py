from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from grades.models import Grade, Professor_Assignment, Student_Assignment


class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')
    list_display_links = ('student', 'course', 'grade')
    search_fields = ('student', 'course', 'grade')
    list_per_page = 25


admin.site.register(Grade, GradeAdmin)


class Professor_AssignmentAdmin(admin.ModelAdmin):
    list_display = ('professor', 'course', 'name', 'date', 'file_uploaded', 'percentage')
    list_display_links =  ('professor', 'course')
    search_fields = ('professor', 'course', 'percentage')
    list_per_page = 25


admin.site.register(Professor_Assignment, Professor_AssignmentAdmin)


class Student_AssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'professor', 'course', 'name', 'date', 'professor_file_uploaded', 'percentage', 'grade', 'submitted', 'file_uploaded')
    list_display_links = ('student','professor', 'course')
    search_fields = ('student','professor', 'course')
    list_per_page = 25


    def professor(self, obj):
        return obj.assignment.professor


    def course(self, obj):
        return obj.assignment.course


    def name(self, obj):
        return obj.assignment.name


    def date(self, obj):
        return obj.assignment.date

    def professor_file_uploaded(self, obj):
        return obj.assignment.file_uploaded

    def percentage(self, obj):
        return obj.assignment.percentage

admin.site.register(Student_Assignment, Student_AssignmentAdmin)
>>>>>>> 87ca4fb (added authenticate functions)

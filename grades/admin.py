from django.contrib import admin
from grades.models import Grade, Professor_Assignment, Student_Assignment


class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')
    list_display_links = ('student', 'course', 'grade')
    search_fields = ('student', 'course', 'grade')
    list_per_page = 25


admin.site.register(Grade, GradeAdmin)


class Professor_AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'professor',
                    'due_date', 'task_file')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'course', 'professor')
    list_per_page = 25


admin.site.register(Professor_Assignment, Professor_AssignmentAdmin)


class Student_AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'professor',
                    'student', 'assignment', 'task_file', 'grade')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'course', 'professor', 'student')
    list_per_page = 25

    def professor(self, obj):
        return obj.assignment.professor

    def course(self, obj):
        return obj.assignment.course

    def name(self, obj):
        return obj.assignment.name


admin.site.register(Student_Assignment, Student_AssignmentAdmin)

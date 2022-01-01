from django.contrib import admin
from files.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'course', 'date')
    list_display_links = ('id', 'filename')
    search_fields = ('filename', 'course')
    list_per_page = 25


admin.site.register(File, FileAdmin)
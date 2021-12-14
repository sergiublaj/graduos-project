from django.contrib import admin
from notifications.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'date')
    list_per_page = 25


admin.site.register(Notification, NotificationAdmin)

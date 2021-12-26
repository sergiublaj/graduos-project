from django.contrib import admin
from invitations.models import Invitation


class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'from_user', 'to_user',
                    'closed', 'accepted', 'date')
    list_display_links = ('id', )
    search_fields = ('course', 'from_user', 'to_user')
    list_per_page = 25


admin.site.register(Invitation, InvitationAdmin)

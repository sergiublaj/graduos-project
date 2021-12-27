from django.contrib import admin
from chats.models import Chat

class ChatAdmin(admin.ModelAdmin):
   list_display = ('user1', 'user2', 'message', 'date')
   list_display_links = ('user1', 'user2')
   search_fields = ('user1', 'user2', 'message')
   list_per_page = 25

admin.site.register(Chat, ChatAdmin)
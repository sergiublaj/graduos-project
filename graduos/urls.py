from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('files/', include('files.urls')),
    path('grades/', include('grades.urls')),
    path('invitations/', include('invitations.urls')),
    path('notifications/', include('notifications.urls')),
    path('forum/', include('forum.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'graduos.views.handle_client_error'
handler500 = 'graduos.views.handle_server_error'

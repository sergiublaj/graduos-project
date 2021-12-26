from django.urls import path
from . import views

urlpatterns = [
    path('invite_participant/<int:course_id>',
         views.invite_participant, name='invite_participant'),
    path('accept_invitation/<int:invitation_id>',
         views.accept_invitation, name='accept_invitation'),
    path('decline_invitation/<int:invitation_id>',
         views.decline_invitation, name='decline_invitation'),
]

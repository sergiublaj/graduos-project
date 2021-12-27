from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from courses.models import Course


class Invitation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_from_user')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_to_user')
    accepted = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.from_user.username + " to " + self.to_user.username

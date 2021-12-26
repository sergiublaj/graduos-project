from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING, default=None)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.title

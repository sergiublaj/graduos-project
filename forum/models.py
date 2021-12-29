from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from datetime import datetime
from courses.models import Course
from users.models import Person


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=DO_NOTHING, default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    post_content = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=datetime.now)




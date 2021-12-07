from django.db import models
from users.models import Student, Professor


class Course(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=8, default="12345678")
    year = models.CharField(max_length=32)
    semester = models.IntegerField()
    description = models.CharField(max_length=128)
    credits_no = models.IntegerField(default=4)
    photo = models.ImageField(blank=True, null=True,
                              upload_to='images/courses/%Y/')
    students = models.ManyToManyField(
        Student, related_name='courses', default=[])
    professors = models.ManyToManyField(
        Professor, related_name='courses', default=[])

    def __str__(self):
        return self.name

from django.db import models
from datetime import datetime

from courses.models import Course

class File(models.Model):
	filename = models.CharField(max_length=128)
	filecontent = models.FileField(upload_to='files/%Y/')
	course = models.ForeignKey(Course, on_delete = models.DO_NOTHING, null = True)
	date = models.DateTimeField(default = datetime.now)

	def __str__(self):
		return self.filename
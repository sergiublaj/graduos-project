from django.db import models
from datetime import datetime
from users.models import Person

class Chat(models.Model):
   user1_id = models.ForeignKey(Person, on_delete = models.DO_NOTHING, related_name='%(class)s_user1')
   user2_id = models.ForeignKey(Person, on_delete = models.DO_NOTHING, related_name='%(class)s_user2')
   message = models.CharField(max_length = 512)
   date = models.DateTimeField(default = datetime.now)


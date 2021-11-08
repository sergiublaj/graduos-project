from django.db import models
from datetime import datetime
from users.models import Person

class Chat(models.Model):
<<<<<<< HEAD
   user1_id = models.ForeignKey(Person, on_delete = models.DO_NOTHING, related_name='%(class)s_user1')
   user2_id = models.ForeignKey(Person, on_delete = models.DO_NOTHING, related_name='%(class)s_user2')
=======
   user1 = models.ForeignKey(Person, on_delete = models.DO_NOTHING, related_name='%(class)s_user1')
   user2 = models.ForeignKey(Person, on_delete = models.DO_NOTHING, related_name='%(class)s_user2')
>>>>>>> 87ca4fb (added authenticate functions)
   message = models.CharField(max_length = 512)
   date = models.DateTimeField(default = datetime.now)


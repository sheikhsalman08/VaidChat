from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChatRoom(models.Model):
	user1 = models.ForeignKey(User, related_name='user1', on_delete=models.SET_NULL, null= True)
	user2 = models.ForeignKey(User, related_name='user2', on_delete=models.SET_NULL, null= True)

	def __str__(self):
		return self.user1.username+' AND '+self.user2.username


class Msg(models.Model):
	txt = models.CharField(max_length=10000,blank=True,null=True)
	time = models.DateTimeField(blank=True,null=True)
	ChatRoom = models.ForeignKey('ChatRoom', on_delete = models.SET_NULL,blank=True, null=True)
	sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, null= True, blank = True)
	receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE, null= True, blank = True)	

	def __str__(self):
		now = self.time
		now_readable = now.strftime("%b %d,%Y | %I:%M:%p")
		return 'By '+self.sender.username+' At '+ now_readable


	def save(self, *args, **kwargs):
		if (self.time is None):
			self.time = datetime.now() + timedelta(hours=6)

		super(Msg, self).save(*args, **kwargs)
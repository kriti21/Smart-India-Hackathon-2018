from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	ACCESS_OPTIONS = (
		('Admin', 'Admin'),
		('Client', 'Client'),
		('Customer', 'Customer'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	access = models.CharField(max_length=10, choices=ACCESS_OPTIONS, null=False)
	
	def __str__(self):
		return self.user.username

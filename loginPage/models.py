from django.db import models

# Create your models here.

class userInfo(models.Model):
	firstName = models.CharField(max_length=30)
	LastName  = models.CharField(max_length=30)
	userName  = models.CharField(max_length=30)
	password  = models.CharField(max_length=30)

	def __str__(self):
		return self.userName
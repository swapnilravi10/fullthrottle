from django.db import models

from django.db import models

class Users(models.Model):
	
	id = models.CharField(primary_key=True, max_length=9) 
	real_name = models.CharField(max_length=45)
	tz = models.CharField(max_length=30)
		
	def __str__(self):
		return self.real_name

class Activity_periods(models.Model):
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
	user = models.ForeignKey(Users, related_name= "activity_periods" , on_delete=models.CASCADE)
	
	def __str__(self):
		return self.start_time

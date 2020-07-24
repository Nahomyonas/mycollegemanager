from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#joined rooms list
class UserRoomsList(models.Model): 
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="userrooms", null=True) 
	roomid=models.CharField(max_length=100) 

	def __str__(self): 
		return self.user
		return self.roomid 


#friendslist
class friends(models.Model):
	connection=models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")
	username=models.CharField(max_length=100)
	userid=models.CharField(max_length=100) 

	def __str__(self): 
		return self.connection 
		return self.username
		return self.userid

class discroom(models.Model): 
	name=models.CharField(max_length=40) 
	key=models.CharField(max_length=7) 
	description=models.CharField(max_length=200, default="") 
	roomtype=models.CharField(max_length=10, default="private")
	bio=models.CharField(max_length=200, null=True)

	def __str__(self): 
		return self.name 
		return self.key 
		return self.description 
		return self.roomtype 
		return self.bio

class roomadmins(models.Model): 
	root=models.ForeignKey(discroom, on_delete=models.CASCADE, related_name="admins", null=True)
	adminname=models.CharField(max_length=100)
	adminid=models.CharField(max_length=10000)  

	def __str__(self): 
		return self.adminname 
		return self.adminid

class roomusers(models.Model): 
	connection=models.ForeignKey(discroom, on_delete=models.CASCADE, related_name="users", null=True)
	username=models.CharField(max_length=100)
	userid=models.CharField(max_length=10000)  
	def __str__(self): 
		return self.username 
		return self.userid


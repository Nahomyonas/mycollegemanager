from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class UserPreferences(models.Model): 
	connection=models.ForeignKey(User, on_delete=models.CASCADE, related_name="preferences", null=True)
	minprice=models.IntegerField(default=5000)
	maxprice=models.IntegerField(default=10000) 

	def __str__(self): 
		return self.connection
		return self.maxprice
		return self.maxprice

class PreferedLocations(models.Model): 
	connection=models.ForeignKey(UserPreferences, on_delete=models.CASCADE, related_name="locations", null=True)
	location=models.CharField(max_length=30)	

	def __str__(self): 
		return self.location

class UserColleges(models.Model): 
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercolleges", null=True)
	name=models.CharField(max_length=100, default="")
	price=models.BigIntegerField(default=0)  
	myrating=models.IntegerField( default=5)
	location=models.CharField(max_length=60, default="") 
	specifiedlocation=models.CharField(max_length=60, default="", null=True, blank=True)
	acceptancerate=models.IntegerField(default=0) 
	deadline=models.DateField(null=True, blank=True) 
	permission=models.BooleanField(default=True)
	def __str__(self): 
		return self.user
		return self.name 
		return self.price  
		return self.myrating 
		return self.location 
		return self.specifiedlocation
		return self.acceptancerate 
		return self.deadline
		return self.permission 



class AllColleges(models.Model):
	name=models.CharField(max_length=100)
	price=models.BigIntegerField(default=0)  
	location=models.CharField(max_length=60, default="") 
	specifiedlocation=models.CharField(max_length=60, default="", null=True, blank=True)
	acceptancerate=models.IntegerField(default=0) 
	deadline=models.DateField(null=True, blank=True) 
	def __str__(self): 
		return self.name 
		return self.price  
		return self.location 
		return self.specifiedlocation
		return self.acceptancerate 
		return self.deadline 



	






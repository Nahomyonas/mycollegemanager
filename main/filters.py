import django_filters
from .models import * 

class CollegeFilter(django_filters.FilterSet): 
	class Meta:
		model=Colleges 
		fields=['myrating', 'name'] 


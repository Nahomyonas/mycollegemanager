from django.urls import path 
from . import views 

urlpatterns=[ 
	path('', views.homepage, name="homepage"),
	path('home', views.homepage, name="home"), 
	path('myco/', views.mylist, name="collegelist"), 
	path('newco/', views.collegedata, name="collegedata"),
	path('coll/<int:id>/', views.coll, name="otherusercoll"), 
	path('mycoll/<int:id>/', views.mycoll, name="coll"), 
	path('mycoll/editdata/<int:id>', views.editdata, name="editcollege"), 
	path('login/csucses/', views.loginsuccess, name="successfullogin"),  
	path('myaccount/', views.myAccount, name="accountpage"),  
	path('storedcolleges/', views.allcolleges, name="colleges from database"),
	path('tops/', views.toppicks, name="divisions"), 

]
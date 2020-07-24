from django.urls import path
from  . import views 

urlpatterns=[
	path('', views.roomhome, name="roomshome"), 
	path('roomsearch/', views.rooms, name="roomsearch"),
	path('roomgenerate/', views.createroom, name="roomcreation"),
	path('idroom/<int:id>', views.roompage, name="room"),
	path('myrooms/', views.myrooms, name="myrooms")
]
from django.shortcuts import render, redirect
from .models import * 


##adding and joining  
def addtomyrooms(user, roomid):
	add=UserRoomsList(roomid=roomid) 
	add.save()
	user.userrooms.add(add) 

def joinroom(username,userid,roomid):
	room=discroom.objects.get(id=roomid) 
	adduser=roomusers(username=username ,userid=userid )
	adduser.save()
	room.users.add(adduser)  

def addadmin(username,userid): 
	addadmin=roomadmins(adminname=username, adminid=userid) 
	addadmin.save()
	discroom.admins.add(addadmin) 


##checks 
def admincheck(roomid, userid):
	isadmin=False
	room=discroom.objects.get(id=roomid)
	for admin in room.admins.all(): 
		if admin.id == userid:  
			isadmin=True 
		else: 
			pass
	if isadmin: 
		return True 
	else: 
		return False 

def usercheck(roomid, userid): 
	verified=False
	room=discroom.objects.get(id=roomid) 
	for user in room.users.all(): 
		if user.id == userid: 
			verified=True 
		else: 
			pass 
	if verified: 
		return True 
	else: 
		return False	


# Create your views here.

def roomhome(response):
	return render(response, "rooms/roomhome.html", {})

def rooms(response):
	alreadyin=[]
	rooms="" 
	search=False
	if response.method == "POST":
		if response.POST.get("submit"):
			query=response.POST.get("search")
			if len(query)>=2:
				rooms=discroom.objects.filter(
					name__icontains=query
					)
				for room in rooms: 
					if usercheck(room.id, response.user.id) or admincheck(room.id,response.user.id):
						alreadyin.append(room.id)

			else: 
				rooms={}
			search=True
		return render(response, "rooms/roomsearch.html", {"rooms":rooms, "search":search, "alreadyin":alreadyin}) 
	if response.method == "GET": 
		if response.GET.get("private"): 
			id=response.GET.get("private")
			pass

		if response.GET.get("public"): 
			roomid=response.GET.get("public") 
			user=response.user
			joinroom(user.username, user.id, roomid)
			addtomyrooms(user, roomid) 
			return redirect("/rooms/idroom/%s" %roomid)

		if response.GET.get("inmyrooms"): 
			roomid=reponse.POST.get("inmyrooms")
			return redirect("/rooms/idroom/%s" %roomid)
	return render(response, "rooms/roomsearch.html", {"search":search}) 


def createroom(response): 
	if response.user.is_authenticated: 
		if response.method == "POST":
			if response.POST.get("save"):
				occupied=False
				name=response.POST.get("name")
				key=response.POST.get("key")
				roomtype=response.POST.get("type").lower() 
				bio=response.POST.get("bio")

				for room in discroom.objects.all(): 
					if room.name == name:
						 occupied=True 
					else:
						occupied=False
				if occupied:
					return render(response, "rooms/makeroom.html", {})

				if not occupied:
					add=discroom(
						name=name, 
						key=key,
						roomtype=roomtype,
						bio=bio
						)
					add.save()
					id=add.id  
					room=discroom.objects.get(id=id) 
					print(room.name)
					addadmin=room.admins(
						adminname=response.user.username,
						adminid= response.user.id
						)
					addadmin.save() 
					addtolist=UserRoomsList(roomid=room.id) 
					response.user.userrooms.add(addtolist)
					return redirect("/rooms")

		return render(response, "rooms/makeroom.html", {}) 
	else: 
		return render(response, "main/notauthenticated",{})

def roompage(response, id): 
	roomid=id
	if usercheck(roomid, response.user.id): 
		return render(response, "rooms/roompage.html", {}) 
	elif admincheck(roomid, response.user.id): 
		return render(response, "rooms/adminroom.html", {}) 
	elif response.user.is_anonymous: 
		return render(response, "main/notauthenticated.html",{})
	else:
		return render(response, "main/notauthenticated.html",{})

	
def myrooms(response): 
	if response.user.is_authenticated: 
		userrooms=response.user.userrooms.all() 
		allrooms=discroom.objects.all() 
		myroomslist=[]
		for room in allrooms: 
			for myroom in userrooms: 
				if room.id == myroom.roomid: 
					myroomslist.append(room)  
		myroomslist=list(set(myroomslist)) 

		return render(response, "rooms/myrooms.html", {"myrooms":myroomslist})

	else: 
		return render(response, "main.notauthenticated.html", {})





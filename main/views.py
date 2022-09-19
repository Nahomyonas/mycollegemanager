from django.shortcuts import render, redirect 
from .models import AllColleges, UserColleges
from django.http import HttpResponse 



# Create your views here. 


def homepage(response): 
	
	if response.user.is_authenticated:
		counter=0
		preference=""
		for pref in response.user.preferences.all():
			counter+=1 
		if counter == 0: 
			preference="notfullfilled" 
		return render(response, "main/home.html", {"preference":preference})
	else: 
		return render(response, "main/home.html", {})

def mylist(response):  
	if response.user.is_authenticated:
		ordered=""
		colleges=response.user.usercolleges.all()
			
		if response.method == "POST":
			by=""
			print(response.POST)
			if response.POST.get("search"): 
				if response.POST.get("by") == "Highest To Lowest":
					by="-"
				elif response.POST.get("by") == "Lowest To Highest": 
					by=""
				sortby=response.POST.get("sortby")
				if sortby == "My Rating":
					ordered=colleges.order_by('%smyrating' %by)
					colleges=ordered 
					method="rating"
				elif sortby == "Acceptance Rate":
					ordered=colleges.order_by('%sacceptancerate' %by)
					colleges=ordered
					method="acceptancerate"  
				elif sortby== "Price(Lowest to Highest)":
					ordered=colleges.order_by('%sprice' %by)
					colleges=ordered  
					method="price"

				return render(response, "main/collegelist.html", {"colleges": colleges, "method":method}) 

			if response.POST.get("save"): 
				return redirect("/newco/")
		return render(response, "main/collegelist.html", {"colleges": colleges}) 
		

	else:  
		return render(response, "main/notauthenticated.html", {}) 

	

#addcolleges
def collegedata(response):  
	if response.user.is_authenticated:
		error = False 
		if response.method == "POST":  
			print(response.POST)  
			if response.POST.get("save"):  
				name=response.POST.get("new") 
				rating=response.POST.get("rating") 
				acceptance=response.POST.get("acceptance") 
				price=response.POST.get("price") 
				location=response.POST.get("loc")  
				specificloc=response.POST.get("specificloc")
				deadline=response.POST.get("deadline") 
				if deadline == "": 
					deadline="1985-10-10"
				if response.POST.get("permission") == "allowed":
					permission=True 
				else: 
					permission=False
				
				

				if name!="":
					new=UserColleges(
						name=name, 
						price=price, 
						myrating=rating,
						location=location,
						specifiedlocation=specificloc,
						acceptancerate=acceptance,
						deadline=deadline,
						permission=permission

						)
					new.save() 
					response.user.usercolleges.add(new) 

					return redirect("/myco") 

		return render(response, "main/collegedata.html", {})  
	else: 
		return render(response, "main/notauthenticated.html", {})  

def coll(response,id): 
	if response.user.is_authenticated:
		college=AllColleges.objects.get(id=id) 
		if response.POST.get("addtolist"):
				response.user.usercolleges.add(college) 
				return redirect("/myco/")
		return render(response, "main/collegepage.html", {"college":college}) 
	else: 
		return render(response, "main/notauthenticated.html",{}) 



def mycoll(response, id):
	if response.user.is_authenticated:
		falsedeadline=False
		college=UserColleges.objects.get(id=id)  
		if college.deadline == "1985-10-10":
			falsedeadline=True
		print(college.deadline)   
		if response.method == "POST": 
			print(response.POST)
			if response.POST.get("delete"): 
				response.user.usercolleges.remove(college)
				return redirect("/myco/") 
		return render(response, "main/mycollegepage.html", {"college":college, "fdeadline": falsedeadline})
	else:
		return render(response, "main/notauthenticated.html", {})  


def editdata(response, id): 
	if response.user.is_authenticated:
		invalid=False
		college=response.user.usercolleges.get(id=id) 
		if response.method == "POST":  
			print(response.POST)  
			if response.POST.get("save"):  
				rating=response.POST.get("rating") 
				acceptance=response.POST.get("acceptance") 
				price=response.POST.get("price") 
				location=response.POST.get("loc") 
				deadline=response.POST.get("deadline")
				if price!="" and location!="" and acceptance!="" and len(acceptance)<3:
					college.price=price 
					college.myrating=rating 
					college.location=location 
					college.acceptancerate=acceptance 
					college.deadline=deadline 
					college.save()
					return redirect("/mycoll/%s/" %college.id) 

		return render(response, "main/editdata.html", {"college":college}) 
	else: 
		return render(response, "main/notauthenticated", {})

def loginsuccess(response): 
	if response.user.is_authenticated: 
		return render(response, "main/successlogin.html", {}) 
	else: 
		return render(response, "main/notauthenticated", {})

def myAccount(response):
	if response.user.is_authenticated:
		counter=0
		preference=""
		for pref in response.user.preferences.all():
			counter+=1 
		if counter == 0: 
			preference="notfullfilled" 
		elif counter == 1: 
			preference="fullfilled"

		return render(response,"main/myaccount.html", {"preference":preference}) 

	else:
		return render(response, "main/notauthenticated.html", {})

def allcolleges(response): 
	if response.user.is_authenticated:
		collegesavail=AllColleges.objects.all()
		mainlist=[]
		for college in collegesavail : 
			for item in response.user.usercolleges.all():
				if college.name != item.name: 
					mainlist.append(college) 
		collegesavail=list(set(mainlist))
		
		if response.method == "GET":
			colleges="" 
			print(response.GET)
			container=[]
			location=response.GET.get("location")
			for college in collegesavail: 
				if college.location == location: 
					container.append(college) 
			if location == "All Colleges": 
				colleges=collegesavail
			else:		
				colleges=list(set(container))
			return render(response, "main/allcolleges.html", {"colleges":colleges}) 

		return render(response, "main/allcolleges.html", {"colleges":collegesavail})

	else: 
		return render(response, "main/notauthenticated.html", {})   

def toppicks(response): 
	if response.user.is_authenticated:
		colleges=response.user.usercolleges.all()
		
		#number of colleges
		numofcolleges=0
		for college in colleges: 
			numofcolleges+=1  
		
		if response.method == "POST": 
			if response.POST.get("search"): 
				print(response.POST) 
				if response.POST.get("sortby") == "My Top Choices": 
					#My Top picks
					title="My Top Choices"
					fieldtitle="My Rating"
					sumofrating=0  
					averagerating=0
					topratings=[]
					for college in colleges: 
						sumofrating+=college.myrating 
					averagerating=sumofrating/numofcolleges
					for college in colleges:
						if college.myrating>=averagerating: 
							topratings.append(college)
					topratings=list(set(topratings))
					return render(response, "main/toppicks.html", {"title":title, "sortby":topratings, "fieldtitle":fieldtitle})

				if response.POST.get("sortby") == "Most Competitive":
					#Most competitive 
					title="Most Competitive"
					fieldtitle="Acceptance Rate"
					sumofacc=0
					competitive=[]
					for college in colleges: 
						sumofacc+=college.acceptancerate
					averageacceptance=sumofacc/numofcolleges
					for college in colleges: 
						if college.acceptancerate<=averageacceptance:  
							competitive.append(college)
					competitive=list(set(competitive)) 
					return render(response, "main/toppicks.html", {"title":title, "sortby":competitive, "fieldtitle":fieldtitle})	


		return render(response, "main/toppicks.html", {})
	else: 
		return render(response,"main/notauthenticated.html", {})








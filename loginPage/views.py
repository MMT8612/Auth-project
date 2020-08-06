from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import userInfo
from django.contrib import messages

# Create your views here.
def login_view(request,*args,**kwargs):
	return render(request,"login.html",{'exists':1})


def signUp_view(request,*args,**kwargs):
	return render(request,"signUp.html",{'exists':0})


def signup_form_submission(request):
	print("form is submitted")
	fname = request.POST["fname"]
	lname = request.POST["lname"]
	uname = request.POST["uname"]
	pwd   = request.POST["pwd"]
	
	if(userInfo.objects.filter(userName=uname).exists()):
		return render(request,"signUp.html",{'exists':1})

	else:
		user_info = userInfo(firstName=fname,LastName=lname,userName=uname,password=pwd)
		user_info.save()
		return render(request, "success_page.html",{'name': fname})

	return render(request,"signUp.html",{'exists':0})


def login_form_submission(request):
	print("Login form is submitted")
	uname = request.POST["uname"]
	pwd   = request.POST["pwd"]
	
	if(userInfo.objects.filter(userName=uname).exists()):
		user = userInfo.objects.get(userName=uname)
		print(user.password)
		if(user.password!=pwd):
			return render(request,login_view,{'exists':0})
		else:
			return render(request, "success_page.html",{'name': user.firstName})
	else:
		return render(request,"login.html",{'exists':0})


def success_page(request):
	return render(request,"success_page.html",{'name':''})

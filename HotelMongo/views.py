from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):

	if request.method == 'POST' :
		first_name = request.POST["first_name"]
		last_name = request.POST['last_name']
		username = request.POST['username']
		password = request.POST[ "password"]
		email =request.POST[ "email"]
		if User.objects.filter(username=username):
				messages.error(request,'username is already taken try different username')
				return redirect('/register/')

		user=User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
		user.save()
		return render(request, 'login.html')
	else:
		return render(request, 'register.html')




# def index(request):
# 	return render(request, 'index.html')



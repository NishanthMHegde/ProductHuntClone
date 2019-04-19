from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):

	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password =request.POST['password'] )
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'accounts/login.html',{'error': 'Sorry, the username or password did not match!'})

	else:

		return render(request,'accounts/login.html')

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request,'accounts/signup.html',{'error': 'Sorry, that username already exists!'})
			except User.DoesNotExist:
				user = User.objects.create_user(username = request.POST['username'] , password = request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'accounts/signup.html',{'error': 'Sorry, that passwords you entered do not match!'})

		return render(request,'accounts/signup.html')
	else:
		return render(request,'accounts/signup.html')

def logout(request):
	if request.method == "POST":
		auth.logout(request)
		return redirect('home')
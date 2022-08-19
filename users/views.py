from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from users.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import User
from movie import templates

# Create your views here.

def index(request):
    return render(request, "movie/movie_list.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Username or password is wrong"
            })

    return render(request, "users/login.html")



def sign_up(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect(reverse("index"))
	else:
	    form = NewUserForm()
	return render (request, "users/sign_up.html", context={"form":form})

def logout_view(request):
    logout(request)
    render(request, "users/login.html")
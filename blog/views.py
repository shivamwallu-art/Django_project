from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    return render(request, 'blog/welcome.html')

@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')

def user_login(request):
    return render(request, 'blog/login.html')
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import redirect

# Create your views here.

def GoogleAuth(request):
    return render(request, 'googlesignin.html')

def home(request):
    response = redirect('/googleauth/')
    return response

def posttoken(request):
    return render(request, 'craccgoogle.html')

def signupf(request):
    return render(request, 'signup.html')

def loginf(request):
    return render(request, 'login.html')

def task1(request):
    return render(request, 'task1.html')

def task1(request):
    return render(request, 'task1.html')


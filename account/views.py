from django.shortcuts import render, redirect, reverse


def login(request):
    return render(request, "account/login.html", {})

def register(request):
    return render(request, "account/register.html", {})

def dashboard(request):
    return render(request, "account/login.html", {})
    

def logout(request):
    return redirect(reverse('realstate:home'))
    
    
from django.shortcuts import render, redirect, reverse
from django.contrib import  messages,auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        #get form values 
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']
        password2  = request.POST['password2']

        #check if password match 
        if password == password2:
            #check username if already exist
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already take by some else")
                return redirect('account:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used.")
                    return redirect("account:register")
                else:
                    #looks good 
                    user = User.objects.create_user(first_name = first_name, last_name=last_name, email=email,\
                        password=password, username= username)
                    #login aftere register 
                    # auth.login(request, user)
                    # messages.success(request, "you are logged in now!!")
                    # return redirect('realstate:home')

                    #but I like to redirect user to login again 
                    user.save()
                    messages.success(request, "You are now registered and can log in ")
                    return redirect('account:login')

        else:
            messages.error(request,"your password dosn't match ")
            return redirect('account:register')
    else:
        return render(request, "account/register.html", {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are logged in now!!")
            return redirect("account:dashboard")
        else:
            messages.error(request,"Invalid credentials!")
            return redirect('account:login')
    else:
        return render(request, "account/login.html", {})


def dashboard(request):
    return render(request, "account/dashboard.html", {})
    

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "you are successfully logged out ")
        return redirect(reverse('account:login'))
    
    
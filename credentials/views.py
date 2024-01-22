from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter (username=username).exists():
                messages.info(request,"Username Exists")
                print("Username already exists")
                return redirect('register')
            elif User.objects.filter (email=email).exists():
                messages.info(request,"Email Id Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                print("User registraton successful !!!")
                return redirect('login')
        else:
            messages.info(request,"Passwords donot match.")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render(request,'form_button.html')
        else:
            messages.info(request,"Invalid credentials")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def form1(request):
    return render(request,'form.html')

def submit(request):
    messages.info(request,"User registration successful")
    return render(request,'form.html')

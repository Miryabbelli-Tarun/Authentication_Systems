from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
User=get_user_model()

# Create your views here.
def register_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password !=confirm_password:
            messages.warning(request,'incorrect password')
            return redirect('register')
        user=User.objects.filter(phone_number=phone_number)
        if  user.exists():
            messages.warning(request,'user already existed')
            return redirect('register')
        # user=authenticate(request,username=phone_number,password=password)
        user=User.objects.create(
            username=username,
            phone_number=phone_number,

        )
        user.set_password(password)
        user.save()
        messages.success(request,'register succesfull')
        return redirect('register')
        
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        user=User.objects.filter(phone_number=phone_number)
        if not user.exists():
            messages.warning(request,'user not exist')
            return redirect('login')
        user=authenticate(request,username=phone_number,password=password)
        if not user:
            messages.warning(request,'incorrect phone_number or password')
            return redirect('login')
        login(request,user)
        return redirect('home')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
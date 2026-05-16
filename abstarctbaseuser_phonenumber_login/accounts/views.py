from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
# Create your views here.
User=get_user_model()
def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone_number=request.POST.get('phone_number')
        confirm_password=request.POST.get('confirm_password')

        if password!=confirm_password:
            messages.warning(request,'incorrect password')
            return redirect('register')
        user=User.objects.filter(phone_number=phone_number)
        if user.exists():
            messages.warning(request,'user already exists')
            return redirect('register')
        user=User.objects.create(phone_number=phone_number,username=username)
        user.set_password(password)
        user.save()
        messages.success(request,'registter succesful')
        return redirect('register')
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        password=request.POST.get('password')
        phone_number=request.POST.get('phone_number')
        user=User.objects.filter(phone_number=phone_number)
        if not user.exists():
            messages.warning(request,'user not exists')
            return redirect('login')
        user=authenticate(request,username=phone_number,password=password)
        if not user:
            messages.warning(request,'incorrect phone number or password')
            return redirect('login')
        login(request,user)
        return redirect('home')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
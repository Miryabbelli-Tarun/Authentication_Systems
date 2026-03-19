from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
User=get_user_model()
# Create your views here.
def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')

        user=User.objects.filter(email=email)
        if user:
            messages.warning(request,'user with mail already exist')
            return redirect('register_view')
        user=User.objects.create(email=email,
                                 phone_number=phone_number,
                                 username=username)
        user.set_password(password)
        user.save()
        messages.success(request,'register succesfully')
        return redirect('register_view')
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=User.objects.filter(email=email)
        if not user.exists():
            messages.warning(request,'user not registered')
            return redirect('register_view')
        user=authenticate(request,email=email,password=password)
        if not user:
            messages.warning(request,'incorrect email or password')
            return redirect('login_view')
        login(request,user)
        messages.success(request,'login succesful')
        return redirect('home')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')
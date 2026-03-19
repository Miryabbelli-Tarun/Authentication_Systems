from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
User=get_user_model()
# Create your views here.
def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone_number=request.POST.get('phone_number')

        user=User.objects.filter(email=email)
        if user.exists():
            messages.warning(request,'user already exist')
            return redirect('register_view')
        user=User.objects.create(
            username=username,
            email=email,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save()
        messages.success(request,'registe succesful')
        return redirect('register_view')
    return render(request,'register.html')


def login_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.filter(email=email)
        if not user.exists():
            messages.warning(request,'user not found')
            return redirect('login_view')
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
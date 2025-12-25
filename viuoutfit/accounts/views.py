from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')  

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

       
        if password != confirm_password:
            return render(request, 'accounts/signup.html', {
                'error': 'Passwords do not match'
            })

        
        if User.objects.filter(username=email).exists():
            return render(request, 'accounts/signup.html', {
                'error': 'Email already registered'
            })

      
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        user.save()

        return redirect('/login/')

    return render(request, 'accounts/signup.html')

def home_view(request):
    return render(request, 'accounts/index.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin/')  
        else:
            return render(
                request,
                'accounts/adminlogin.html',
                {'error': 'Invalid admin credentials'}
            )

    return render(request, 'accounts/adminlogin.html')



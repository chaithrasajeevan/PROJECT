from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import csv
import os

CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fashion_dataset.csv')

def ai_recommendation(user_input):
    dataset = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dataset.append(row)

    matches = []
    for row in dataset:
        if (
            row['gender'].lower() == user_input['gender'].lower() and
            row['body_type'].lower() == user_input['body_type'].lower() and
            row['occasion'].lower() == user_input['occasion'].lower() and
            row['weather'].lower() == user_input['weather'].lower() and
            row['style'].lower() == user_input['style'].lower() and
            (row['top_color'].lower() == user_input['color'].lower() or
             row['bottom_color'].lower() == user_input['color'].lower())
        ):
            matches.append(row)
    return matches

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('outfits') 
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid email or password'})

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
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=email).exists():
            return render(request, 'accounts/signup.html', {'error': 'Email already registered'})

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
            return render(request, 'accounts/adminlogin.html', {'error': 'Invalid admin credentials'})

    return render(request, 'accounts/adminlogin.html')



@login_required 
def outfit_view(request):
    matches = []
    if request.method == 'POST':
        user_input = {
            'gender': request.POST.get('gender'),
            'body_type': request.POST.get('body_type'),
            'occasion': request.POST.get('occasion'),
            'weather': request.POST.get('weather'),
            'style': request.POST.get('style'),
            'color': request.POST.get('color')
        }

        print(user_input)

        matches = ai_recommendation(user_input)

    return render(request, 'accounts/outfits.html', {'matches': matches, 'user': request.user})

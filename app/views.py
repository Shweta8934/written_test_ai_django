# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm # Abhi hum yeh form banayenge

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard') # Agar pehle se logged in hai to dashboard pe bhej do
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # CustomUser model aur email se authenticate karo
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # User mil gaya aur password sahi hai
                login(request, user)
                return redirect('dashboard')
            else:
                # Authentication fail
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'title': 'Login'})

@login_required # Sirf logged in users hi access kar payenge
def dashboard(request):
    context = {
        'user': request.user,
        'title': 'User Dashboard',
        'content': 'Welcome to your secured dashboard!'
    }
    return render(request, 'dashboard.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')
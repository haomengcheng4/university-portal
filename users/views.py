from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib import messages

def homepage_view(request):
    return render(request, 'homepage.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on role
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'admin':
                return redirect('admin_dashboard')

            return redirect('home')  # Default redirect if role is missing
    else:
        form = CustomUserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Role-based decorators
def student_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.role != 'student':
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrap

def teacher_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.role != 'teacher':
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrap

def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.role != 'admin':
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrap

# Dashboard Views
@login_required
@student_required
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')

@login_required
@teacher_required
def teacher_dashboard(request):
    return render(request, 'users/teacher_dashboard.html')

@login_required
@admin_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')
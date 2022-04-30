"""Views for the different pages to be rendered"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import (
    authenticate, login, logout, update_session_auth_hash)


def login_page(request):
    """Login Page view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context = {}

    return render(request, 'accounts/login.html', context)


def logout_user(request):
    """User Logout View"""
    logout(request)
    return redirect('home')


def register_user(request):
    """
    User Registration Form View.
    Used The Pylot article to help create this view.
    """

    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(
                email=email, username=username, password=password)
            login(request, user)
            messages.success(
                request, "Welcome, you can now share your own posts!")
            return redirect('home')
        else:
            messages.error(
                request, 'Passwords not a match or username taken.')
            form = UserCreationForm()
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def change_password(request):
    """Manage User Account to Change Password and Delete Account"""
    form = PasswordChangeForm(user=request.user, data=request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated")
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            messages.error(
                request, "Incorrect Password or New Passwords do not match")

    return render(request, 'accounts/password_change.html', {'form': form})

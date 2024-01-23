from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, CustomUserCreationForm
from django.contrib import messages


# Home page
def index(request):
    return render(request, 'index.html')


# Signup page
def user_signup(request):
    registered_user = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            User = get_user_model()
            registered_user = User.objects.get(email=form.cleaned_data['email'])
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'registered_user': registered_user})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, '')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


# Logout page
def user_logout(request):
    logout(request)
    return redirect('logout')

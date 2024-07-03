from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ContactForm


def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Account has been created for {username} successfully!')
            user = authenticate(username=username, password=password)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'You have been logged in successfully!')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    return render(request, 'users/logout.html')
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            
            send_mail(
                f"New contact from {name}",
                message,
                email,
                ['nilachakra2011@gmail.com'],
            )
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact/')  
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})

@login_required
def menu(request):
    return render(request, 'users/menu.html')

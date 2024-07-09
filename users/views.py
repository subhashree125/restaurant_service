from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .forms import UserRegisterForm, ContactForm
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


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
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'username': user.username,
        'email': user.email,  
        'user_form': user_form,      
    }    
    return render(request, 'users/profile.html', context)
@login_required
def order_summary(request):
    user = request.user
    context = {
        'username': user.username,
    }
    return render(request, 'users/order_summary.html', context)
@login_required
def confirmation(request):
    return render(request, 'users/confirmation.html')
@login_required
def delete_user(request):
    user = request.user
    if user.is_authenticated:
        username = user.username
        user.delete()
        
        response = redirect('users/home.html')
        response.set_cookie('deleteOrderHistory', user.username, path='/')
        return response
    else:
        return redirect('users/login.html')

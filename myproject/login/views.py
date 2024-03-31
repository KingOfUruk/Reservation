from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login , logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Assuming 'home' is the name of your home view
        else:
            # Handle invalid login credentials
            # For example, you can render the login form again with an error message
            return render(request, 'login/login.html', {'error_message': 'Invalid username or password'})
    else:
        # If it's a GET request, just render the login form
        return render(request, 'login/login.html')

def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    return redirect('login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home_view(request):
    username = request.user.username
    return render(request,'home.html',{'username':username})
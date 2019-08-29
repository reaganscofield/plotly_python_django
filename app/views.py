from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Account
import random 
from . import plots


# home page render function
def index(request):
    return render(request, 'pages/index.html')

# read data from sqlite
def read(request):
    data = { "data": Account.objects.all() }
    return render(request, 'pages/read_db.html', data)

# carousel render function 
def carousel(request):
    return render(request, 'pages/carousel.html')


# dashboard function 
def dashboard(request):
  return render(request, 'pages/dashboard.html')


# plotly graph render
def plotlygraph(request):
    context = {
        'piechart': plots.pie_chart()
    }
    return render(request, 'pages/plotlygraph.html', context)


def register(request):
    if request.method == 'POST':
        # get user input
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username is taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # check if email is taken
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # create user 
                    user = User.objects.create_user(
                            username=username, 
                            password=password,
                            email=email, 
                            first_name=first_name, 
                            last_name=last_name
                    )
                    user.save()
                    # redirect user to login 
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')


# login function
def login(request):
    # check request method if POST perform action
    if request.method == 'POST':
        # getting user password and username
        username = request.POST['username']
        password = request.POST['password']

        # authenticated user
        user = auth.authenticate(username=username, password=password)

        # if success let redirect user to welcome
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')

            # auto create random data
            data = Account.objects.create(
               user_id = user,
               account_number = random.randint(1,3445565632),
               trasaction_day_record = "23455, 5678, 1234,  12, 456",
               weekly_day_record = "Monday, Tuesday, Wednesday, Thursday, Friday"
            )
            data.save()

            return redirect('dashboard')
        # if not success redirect back to login 
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    # if method is not POST redirect back to login 
    else:
        return render(request, 'pages/login.html')


# logout function
def logout(request):
  # check for method if POST
  if request.method == 'POST':
    # logout user
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    # redirect to home
    return redirect('index')






 
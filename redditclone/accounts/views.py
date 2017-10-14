from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmation_password']:

            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already be taken!'})

            except User.DoesNotExist:

                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                login(request, user)

                return render(request, 'accounts/signup.html')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords didn\'t match!'})
    else:
        return render(request, 'accounts/signup.html')


def user_login(request):
    if request.method == 'POST':

        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)

            return render(request, 'posts/home.html')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and password didn\'t match!'})

    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
    else:
        return render(request,'accounts/logout.html')

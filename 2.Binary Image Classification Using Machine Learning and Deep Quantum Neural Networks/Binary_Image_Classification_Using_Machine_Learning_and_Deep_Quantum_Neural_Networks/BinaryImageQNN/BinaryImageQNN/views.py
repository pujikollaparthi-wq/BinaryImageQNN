from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm


# =========================
# HOME PAGE
# =========================

def index(request):

    return render(request, 'index.html')


# =========================
# ADMIN LOGIN PAGE
# =========================

def AdminLogin(request):

    return render(request, 'AdminLogin.html')


# =========================
# USER LOGIN PAGE
# =========================

def UserLogin(request):

    return render(request, 'UserLogin.html')


# =========================
# USER REGISTER PAGE
# =========================

def UserRegister(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Registration Successful. Please Login.")

            return redirect('UserLogin')

        else:

            messages.error(request, "Registration Failed. Please check details.")

    else:

        form = UserRegistrationForm()

    return render(request, 'UserRegister.html', {'form': form})
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from users.forms import RegisterForm, LoginForm, BMIForm, cal_height, cal_bmi


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.warning(request, f"{form.cleaned_data['username']} is already in use")
                return redirect(reverse('users:login'))
            user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, f'{user.username} successfully created!')
            return redirect(reverse('users:login'))
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                messages.info(request, 'Successfully logged in!')
                return redirect(reverse('users:profile'))
            else:
                messages.error(request, 'Bad authentication.....')
                return redirect(reverse('users:login'))

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect(reverse('users:login'))


@login_required
def profile(request):
    bmi = ''
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            feet = form.cleaned_data['feet']
            print(f'feet:{feet}')
            inches = form.cleaned_data['inches']
            print(f'inches:{inches}')
            inch_height = cal_height(feet, inches)
            weight = form.cleaned_data['weight']

            meter_height = cal_height(feet, inches) * 0.0254
            print(f'meter_height:{meter_height}')
            kg_weight = form.cleaned_data['weight'] * 0.453592
            print(f'kg_weight:{kg_weight}')

            bmi = cal_bmi(meter_height, kg_weight)

            messages.success(request, f'Your BMI is {bmi}')
        else:
            messages.error(request, 'Check your info and try again')

    else:
        form = BMIForm()
    return render(request, 'users/profile.html', {'form': form})


def trump(request):
    return render(request, 'users/trump.html')

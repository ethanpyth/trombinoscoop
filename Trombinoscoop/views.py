from datetime import datetime
from django.shortcuts import render, redirect
from Trombinoscoop.forms import LoginForm


def welcome(request):

    return render(request, 'welcome.html', {'current_date_time': datetime.now})


def login(request):
    if len(request.POST):
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('welcome/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

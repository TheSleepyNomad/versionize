from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(username=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('lk'))
    else:
        form = UserLoginForm()
    context = {'title': 'Login',
               'form': form}
    return render(request, 'user/login.html', context)


def lk(request):
    return render(request, 'user/lk.html')

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import User


# login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_category_list')
        else:
            return render(request=request,
                          template_name='login.html',
                          context={'login_error': True})
    else:
        return render(request=request,
                      template_name='login.html')

# logout
def logout_user(request):
    logout(request)
    return redirect('home')

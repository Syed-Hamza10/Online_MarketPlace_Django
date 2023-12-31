from django.shortcuts import render, redirect
from main.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request,'accounts/signup.html',{
        'form' : form
    })


from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'yourtodo/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                redirect('currenttodos')
            except IntegrityError:
                return render(request, 'yourtodo/signup.html',
                              {'form': UserCreationForm(), 'error': 'That username has already has taken, Please '
                                                                    'choose a new Username.'})
        else:
            return render(request, 'yourtodo/signup.html',
                          {'form': UserCreationForm(), 'error': 'Password did not Match'})


def currenttodos(request):
    return render(request,'yourtodo/currenttodos.html')
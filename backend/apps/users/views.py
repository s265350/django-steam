from django.shortcuts import redirect
from steamauth import *
from django.contrib.auth import login, logout
from .user import process
from django.conf import settings

USE_SSL = getattr(settings, 'USE_SSL', False)

# Create your views here.
def signin(request): # GET /login
    return auth('/api/users/callback', use_ssl=USE_SSL)

def callback(request): # GET /process
    steam_id = get_uid(request.GET)
    user = process(steam_id)

    if user is not None:
        # login success
        login(request, user)
    # login failed
    return redirect('/')

def signout(request):
    logout(request)
    return redirect('/')
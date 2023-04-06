from django.utils import timezone
from django.db import models
from django.conf import settings
from .models import SteamUser, Coach
from steam import Steam

STEAM_API_KEY = getattr(settings, 'STEAM_API_KEY', None)
steam = Steam(STEAM_API_KEY)

def process_steam_login(steam_id):
    if steam_id is None:
        # login failed
        return None
    # login success
    user = get_steam_user(steam_id)
    user.last_login = models.DateTimeField(timezone.now)
    user.save()
    return user

def get_steam_user(steam_id):
    try:
        return SteamUser.objects.get(username=steam_id)
    except SteamUser.DoesNotExist:
        user = SteamUser.objects.create_user(username=steam_id)
        player = steam.users.get_user_details(steam_id).get('player') # Web API call

        user.profile.personaname=player.get('personaname')
        user.profile.profileurl=player.get('profileurl') #https://steamcommunity.com/profiles/{steam_id}

        user.profile.avatar=player.get('avatar')
        user.profile.avatarmedium=player.get('avatarmedium')
        user.profile.avatarfull=player.get('avatarfull')

        user.profile.communityvisibilitystate=player.get('communityvisibilitystate')
        user.profile.personastate=player.get('personastate')

        user.profile.save()
        return user

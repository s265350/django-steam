from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    # defining the different roles
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STEAMUSER = 'STEAMUSER', 'SteamUser'
        COACH = 'COACH', 'Coach'
    # default role
    base_role = Role.ADMIN
    # base infos
    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('Last login'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    role = models.CharField('Role', max_length=50, choices=Role.choices)
    # creating the fields# others
    steam_id = models.CharField(_('Steam ID'), max_length=17, unique=True, null=True, blank=True)
    email = models.EmailField(_('E-mail'), null=False, blank=True)
    age = models.IntegerField(null=True, blank=True)

    # functions
    def __str__(self): # record shown in Users table in the /admin route
        if (self.role == 'ADMIN'):
            return str(self.username)
        if (self.role == 'STEAMUSER'):
            return str(self.steam_id) + ' - ' + str(self.email)
        if (self.role == 'COACH'):
            return str(self.email)

    # overriding  save function
    def save(self, *args, **kwargs):
        if not self.pk: # primary key
            self.role = self.base_role
            return super().save(*args, **kwargs)

class SteamUser(User):
    pass

class SteamUserProfile(models.Model):
    pass

class Coach(User):
    pass

class CoachProfile(models.Model):
    pass
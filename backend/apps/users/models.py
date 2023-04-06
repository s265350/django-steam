from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class SteamUserManager(BaseUserManager):
    # handles operations on SteamUser only
    def _create_user(self, username, **extra_fields):
        '''
        Creates and saves a User with the given steam_id
        '''
        try: # python social auth provides an empty email param, which cannot be used here
            del extra_fields['email']
        except KeyError:
            pass
        
        if not username:
            raise ValueError('The given Steam ID must be set')

        user = self.model(username=username, steam_id=username, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, username, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, **extra_fields)

    # returns all steam users
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STEAMUSER)

class SteamUser(User):
    pass

class SteamUserProfile(models.Model):
    pass

class Coach(User):
    pass

class CoachProfile(models.Model):
    pass
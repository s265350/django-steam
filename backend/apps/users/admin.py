from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SteamUserProfile, CoachProfile

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'age', 'role', 'steam_id')})
UserAdmin.fieldsets = tuple(fields)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(SteamUserProfile)
admin.site.register(CoachProfile)

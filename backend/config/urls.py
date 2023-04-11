"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from apps.home import views as home
from apps.users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
]

# web patterns
urlpatterns += [
    path('', home.home, name='home'),
]

# user login patterns
urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/users/signup', users.signup, name='signup'),
    path('api/v1/users/callback', users.callback, name='callback'),
]

# from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from userprofile.views import login, register


urlpatterns = [
    path('users/', register),
    path('login/', login),
    # path('admin/', admin.site.urls),
]

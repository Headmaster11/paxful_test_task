from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from userprofile.views import login, register, statistics
from wallets.urls import router as wallets_router
from transactions.urls import router as transaction_router


urlpatterns = [
    path('users/', register),
    path('login/', login),
    path('statistics/', statistics),
    url(r'^wallets/', include(wallets_router.urls)),
    url(r'^transactions/', include(transaction_router.urls)),
    path('admin/', admin.site.urls),
]

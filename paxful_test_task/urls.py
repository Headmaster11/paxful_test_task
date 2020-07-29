from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from userprofile.views import login, register, statistics
from wallets.urls import router as wallets_router
from transactions.urls import router as transaction_router


schema_view = get_schema_view(
   openapi.Info(
      title="Paxful test task API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('users/', register),
    path('login/', login),
    path('statistics/', statistics),
    url(r'^wallets/', include(wallets_router.urls)),
    url(r'^transactions/', include(transaction_router.urls)),
    path('admin/', admin.site.urls),
    url(r'^', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

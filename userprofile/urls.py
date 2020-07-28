from rest_framework.routers import SimpleRouter

from userprofile.views import login, register


router = SimpleRouter()
router.register(r'', login, basename='users')
router.register(r'', register, basename='users')

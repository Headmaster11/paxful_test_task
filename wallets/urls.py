from rest_framework.routers import SimpleRouter

from wallets.views import WalletViewSet


router = SimpleRouter()
router.register(r'', WalletViewSet)

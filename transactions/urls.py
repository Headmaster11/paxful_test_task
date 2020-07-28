from rest_framework.routers import SimpleRouter

from transactions.views import TransactionViewSet


router = SimpleRouter()
router.register(r'', TransactionViewSet)

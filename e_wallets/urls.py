from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from e_wallets import views
from e_wallets.views import TransactionView

# router = routers.DefaultRouter()
# router.register('transaction', views.TransactionView,basename="transact")
#
# urlpatterns = router.urls
router = DefaultRouter()
router.register('transaction',views.TransactionView,basename='transactions')

urlpatterns =router.urls


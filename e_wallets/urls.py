from django.urls import path, include
from rest_framework_nested import routers

from e_wallets import views
from e_wallets.views import TransactionView

# router = routers.DefaultRouter()
# router.register('transaction', views.TransactionView,basename="transact")
#
# urlpatterns = router.urls


urlpatterns = [
    path('transfer/',  TransactionView.as_view(), name='transfer'),
]

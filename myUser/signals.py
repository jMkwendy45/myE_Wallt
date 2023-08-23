from django.db.models.signals import post_save
from django.dispatch import receiver

from e_wallets.models import Wallet
from myUser.models import WalletUser


@receiver(post_save, sender=WalletUser)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(
            user=instance, wallet_number=instance.phone_number[1:]
        )


# @receiver(post_save, sender=WalletUser)
# def create_wallet(sender, instance, created, **kwargs):
#     if created and instance.phone_number:
#         Wallet.objects.create(
#             user=instance, wallet_number=instance.phone_number[1:]
#         )

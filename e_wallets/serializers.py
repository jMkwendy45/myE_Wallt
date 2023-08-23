from abc import ABC

from rest_framework import serializers

from e_wallets.models import Transaction, Wallet
from myUser.serializers import CreateUserSerializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'balance', 'transaction',  'wallet_number']

        user = CreateUserSerializer()


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type', 'status', 'datetime', 'amount']
        wallet = WalletSerializer()

class TransactionActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields=[]


from abc import ABC

from rest_framework import serializers

from e_wallets.models import Transaction, Wallet
from myUser.serializers import CreateUserSerializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'balance', 'transaction', 'wallet_number']

        user = CreateUserSerializer()


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type', 'status', 'datetime', 'amount']
        wallet = WalletSerializer()


class TransactionActivitySerializer(serializers.ModelSerializer):
    Transaction_type = [
        ('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT'),
        ('TRANSFER', 'TRANSFER')


        ]
    wallet_number =serializers.CharField(max_length=10,required=False)
    amount =serializers.DecimalField(max_digits=11,decimal_places=2)
    transaction_type =serializers.ChoiceField(choices=Transaction_type,default='DEBIt')
    description =serializers.CharField(max_length=200,required=False)


    def validate(self,data):
        if data.get('transaction_type')=='TRANSFER' and data.get('wallet_number') is None:
            raise serializers.ValidationError(
                "Wallet number must be provided for TRANSFER transction type"
            )
        return super().validate(data)




    class Meta:
        model = Transaction
        fields = []

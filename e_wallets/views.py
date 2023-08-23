from decimal import Decimal

from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from e_wallets.models import Wallet, Transaction
from e_wallets.serializers import TransactionSerializer, WalletSerializer, TransactionActivitySerializer


class TransactionView(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionActivitySerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        user = self.request.user
        wallet = get_object_or_404(Wallet, user=user.id)
        balance = wallet.balance
        transaction_details = {}
        serializer = TransactionActivitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.data['transfer_type'] == 'CREDIT':
                balance = wallet.balance + Decimal(serializer.data['amount'])
            elif serializer.data['transaction_type'] == 'DEBIT':
                if Decimal(serializer.data['amount']) < wallet.balance:
                    balance = wallet.balance - Decimal(serializer.data['amount'])
                else:
                    return Response(data="Insufficient funds", status=status.HTTP_400_BAD_REQUEST)
            elif serializer.data['transacction_type'] == 'TRANSFER':
                if Decimal(serializer.data['amount']) < wallet.balance:
                    balance = wallet.balance - Decimal(serializer.data['amount'])
                else:
                    return Response(data="Insufficient funds", status=status.HTTP_400_BAD_REQUEST)
                try:
                    wallet_to_transfer_to = Wallet.objects.get(
                        wallet_number=serializer.data['wallet_number'])
                except Wallet.DoesNotExist:
                    return Response(data={"message": "Account with the wallet number not found"},
                                    status=status.HTTP_400_BAD_REQUEST)
                transferred_balance = wallet_to_transfer_to.balance + \
                                      Decimal(serializer.data['amount'])
                Wallet.objects.filter(user_id=wallet_to_transfer_to.user_id).update(
                    balance=transferred_balance)

            else:
                return Response(data="Invalid transaction", status=status.HTTP_400_BAD_REQUEST)
            Wallet.objects.filter(user_id=user.id).update(balance=balance)
            transaction_details['New Balance'] = balance
            transaction_details['Transaction type'] = serializer.data['transaction_type']
            transaction_details['Name'] = f"{wallet.user.last_name} {wallet.user.first_name}"
            transaction_details['Time'] = wallet.time_created
            transaction_details['Amount'] = serializer.data['amount']
            transaction_details['Description'] = serializer.data.get(
                'description', "Transaction Description Not Provided")

            transactions = Transaction()
            transactions.wallet = wallet
            transactions.amount = serializer.data['amount']
            transactions.transaction_type = serializer.data['transaction_type']
            transactions.description = serializer.data.get(
                'description', "Transaction Description Not Provded"
            )
            transactions.save()
            return Response(data=transaction_details, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(data="Method not supported", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request):
        return Response(data="Method not supported", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def post(self, request, *args, **kwargs):
    #     sender_wallet_number = request.data.get('wallet_number')
    #     receiver_wallet_number = request.data.get('wallet_number')
    #     transfer_amount = Decimal(request.data.get('amount'))
    #
    #     sender_wallet = get_object_or_404(Wallet, wallet_number=sender_wallet_number)
    #     receiver_wallet = get_object_or_404(Wallet, wallet_number=receiver_wallet_number)
    #
    #     if sender_wallet.balance < transfer_amount:
    #         return Response({'message': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     sender_wallet.balance -= transfer_amount
    #     receiver_wallet.balance += transfer_amount
    #
    #     sender_wallet.save()
    #     receiver_wallet.save()
    #
    #     Transaction.objects.create(
    #         type='DEBIT',
    #         status='SUCCESSFUL',
    #         amount=transfer_amount,
    #         wallet=sender_wallet,
    #     )
    #     Transaction.objects.create(
    #         type='CREDIT',
    #         status='SUCCESSFUL',
    #         amount=transfer_amount,
    #         wallet=receiver_wallet,
    #     )
    #
    #     return Response({'message': 'Transfer successful'}, status=status.HTTP_200_OK)

#     class WithdrawView(APIView):
#         def post(self, request, *args, **kwargs):
#             wallet_number = request.data.get('wallet_number')
#             withdrawal_amount = Decimal(request.data.get('amount'))
#
#             wallet = get_object_or_404(Wallet, wallet_number=wallet_number)
#
#             if wallet.balance < withdrawal_amount:
#                 return Response({'message': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

#             wallet.balance -= withdrawal_amount
#             wallet.save()
#
#             Transaction.objects.create(
#                 type='DEBIT',
#                 status='SUCCESSFUL',
#                 amount=withdrawal_amount,
#                 wallet=wallet,
#             )
#
#             return Response({'message': 'Withdrawal successful'}, status=status.HTTP_200_OK)
#
# #     def post(self, request):
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             sender_wallet = serializer.validated_data['sender']
#             receiver_wallet = serializer.validated_data['receiver']
#             amount = serializer.validated_data['amount']
#
#             if sender_wallet.balance < amount:
#                 return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
#
#             sender_wallet.balance -= amount
#             receiver_wallet.balance += amount
#             sender_wallet.save()
#             receiver_wallet.save()
#
#             Transaction.objects.create(wallet=sender_wallet, type='transfer', status='completed', amount=-amount)
#             Transaction.objects.create(wallet=receiver_wallet, type='transfer', status='completed', amount=amount)
#
#             return Response({"message": "Transfer successful"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class WalletViewSet(ModelViewSet):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer

# class TransferView(APIView):
#     def post(self, request):
#         serializer = TransferSerializer(data=request.data)
#         if serializer.is_valid():
#             sender_wallet = serializer.validated_data['sender_wallet']
#             receiver_wallet = serializer.validated_data['receiver_wallet']
#             amount = serializer.validated_data['amount']
#
#             if sender_wallet.balance < amount:
#                 return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
#
#             sender_wallet.balance -= amount
#             receiver_wallet.balance += amount
#             sender_wallet.save()
#             receiver_wallet.save()
#
#             sender_transaction = Transaction.objects.create(wallet=sender_wallet, type='transfer', status='completed', amount=-amount)
#             receiver_transaction = Transaction.objects.create(wallet=receiver_wallet, type='transfer', status='completed', amount=amount)
#
#             return Response({"message": "Transfer successful"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class WithdrawView(APIView):
#     def post(self, request):
#         serializer = WithdrawSerializer(data=request.data)
#         if serializer.is_valid():
#             wallet = serializer.validated_data['wallet']
#             amount = serializer.validated_data['amount']
#
#             if wallet.balance < amount:
#                 return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
#
#             wallet.balance -= amount
#             wallet.save()
#
#             withdrawal_transaction = Transaction.objects.create(wallet=wallet, type='withdraw', status='completed', amount=-amount)
#
#             return Response({"message": "Withdrawal successful"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

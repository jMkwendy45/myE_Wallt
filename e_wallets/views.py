from decimal import Decimal

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from e_wallets.models import Wallet, Transaction
from e_wallets.serializers import TransactionSerializer, WalletSerializer


class TransactionView(ModelViewSet):
    queryset =  Transaction.objects.all()
    serializer_class = TransactionActivitySerializer





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

from uuid import uuid4

from django.db import models

from wallet import settings


# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    wallet_number = models.CharField(max_length=10, primary_key=True, unique=True)
    # time_created=models.DateTimeField(auto_now_add=True,default=True)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
        ('DEPOSIT','DEPOSIT')
    ]
    TRANSACTION_STATUS = [
        ('PENDING', 'Pending'),
        ('SUCCESSFUL', 'Successful'),
        ('DECLINED', 'declined'),
    ]
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE, default='Credit')
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS, default='Pending')
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=7)
    reference_number = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='transactions', default=0)
    pin = models.CharField(max_length=4, default=0)
    description = models.CharField(max_length=255, blank=True, null=True)
    transaction_time = models.CharField(max_length=255,blank=True,null=True)

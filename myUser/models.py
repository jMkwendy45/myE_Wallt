from django.contrib.auth.models import AbstractUser
from django.db import models
from wheel.metadata import _


# Create your models here.

class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)


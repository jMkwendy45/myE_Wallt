# Generated by Django 4.2.4 on 2023-08-23 07:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('type', models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], default='Credit', max_length=6)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SUCCESSFUL', 'Successful'), ('DECLINED', 'declined')], default='Pending', max_length=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('reference_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pin', models.CharField(default=0, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('wallet_number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]

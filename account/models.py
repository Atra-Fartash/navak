from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


class OTP(models.Model):
    otp = models.IntegerField()
    phone_number = models.CharField(max_length=12)
    expire_date = models.DateTimeField(null=True, blank=True)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    payment_code = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=2, choices=[("a", "IN"), ("b", "OUT")])

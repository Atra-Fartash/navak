from account.models import Profile, Transaction
from rest_framework.serializers import ModelSerializer



class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'email', 'date_of_birth']


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'date', 'payment_code']
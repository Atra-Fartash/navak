from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from account.serializers import TransactionSerializer, ProfileSerializer
from account.models import Transaction, Profile, Wallet
from rest_framework import permissions
import random



class ProfileListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=user)
    

class TransactionView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
        user_wallet = Wallet.objects.get(user=self.request.user)
        wallet_amount = user_wallet.amount
        serializer.save(
            user=self.request.user,
            payment_code=random.randint(1000, 9999),
            payment_type="b",
            amount=(
                serializer.validated_data["amount"]
                if serializer.validated_data["amount"] < wallet_amount
                else wallet_amount
            ),
        )
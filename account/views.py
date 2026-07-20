from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from account.serializers import TransactionSerializer, ProfileSerializer
from account.models import Transaction, Profile, Wallet, OTP
from rest_framework import permissions
import random
from django.core.cache import cache
from rest_framework.response import Response
from datetime import timedelta
from django.utils.timezone import now
from navak.settings import OTP_LIFETIME
from django.shortcuts import render



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


class GetOTP(APIView):

    def post(self, request):
        genrated_otp = random.randint(1000, 9999)
        phone_number = request.data.get("phone_number")
        cache.set(phone_number, genrated_otp, timeout=OTP_LIFETIME)
        otp_object = OTP.objects.create(
            otp = genrated_otp,
            phone_number = request.data.get('phone_number'),
        )
        # SEND OTP TO USER BY SMS
        otp_object.expire_date = now() + timedelta(seconds=OTP_LIFETIME)
        otp_object.save()
        return Response("OTP sent!")


class CheckOTP(APIView):

    def post(self, request):
        input_otp = request.data.get("otp")
        input_phone_number = request.data.get("phone_number")
        saved_otp = cache.get(input_phone_number)
        saved_otp = OTP.objects.get(phone_number=input_phone_number)
        if saved_otp.otp == input_otp and saved_otp.expire_date >= now():
            saved_otp.delete()
            return Response('OK')
        else:
            return Response('Something is wrong!')


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


def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')
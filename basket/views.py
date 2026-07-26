from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import serializers
from basket.serializers import BasketItemSerializer
from basket.models import Basket, BasketItem, Discount
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import render



def _update_basket_price(basket):
    basket.total_price = 0
    basket.save()
    for item in BasketItem.objects.filter(basket=basket):
        product = item.electronic_book or item.audio_book or item.podcast
        if product:
            basket.total_price += product.price
    basket.save()


class AddBasketItem(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BasketItemSerializer
    queryset = BasketItem.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        product = (
            serializer.validated_data.get('electronic_book') or
            serializer.validated_data.get('audio_book') or
            serializer.validated_data.get('podcast')
        )
        
        basket, create = Basket.objects.get_or_create(
            owner = user,
            is_paid = False,
            defaults={
                'total_price' : 0,
                'final_price' : 0,
            }
        )
        
        existing = BasketItem.objects.filter(basket=basket).filter(
        electronic_book=serializer.validated_data.get('electronic_book'),
        audio_book=serializer.validated_data.get('audio_book'),
        podcast=serializer.validated_data.get('podcast'),
    )
        if existing.exists():
            raise serializers.ValidationError('This item is already in your basket.')

        serializer.save(owner=self.request.user, basket=basket)
        _update_basket_price(basket)


class BasketItemList(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BasketItemSerializer
    queryset = BasketItem.objects.all()

    def get_queryset(self):
        return BasketItem.objects.filter(owner=self.request.user)


class DeleteBasketItem(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BasketItemSerializer
    queryset = BasketItem.objects.all()

    def get_queryset(self):
        return BasketItem.objects.filter(owner=self.request.user)


from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

class CheckoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        basket = Basket.objects.filter(owner=request.user, is_paid=False).first()
        if not basket:
            return Response({'detail': 'سبد خرید خالی است'}, status=400)
        basket.is_paid = True
        basket.save()
        return Response({'detail': 'سفارش ثبت شد'})


class DiscountAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        code_str = request.data.get('code')
        if not code_str:
            return Response({'detail': 'No discount code provided'}, status=400)
        
        try:
            discount = Discount.objects.get(code = code_str)
        except Discount.DoesNotExist:
            return Response({'detail' : 'Invalid discount code'}, status=400)
        
        if discount.discount_type == 'percent':
            discount_amount = Basket.total_price * (discount.value / 100)
        else:
            discount_amount = discount.value
        
        Basket.discount = discount
        Basket.final_price = max(Basket.total_price - discount_amount, 0)
        Basket.save()
        discount.usage_count += 1
        discount.save()
        return Response({
            'detail' : 'Discount code applied successfully',
            'discount' : discount.code,
            'final_price' : Basket.final_price
        }, status=200)
    

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')
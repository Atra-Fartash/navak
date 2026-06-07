from basket.models import BasketItem
from rest_framework.serializers import ModelSerializer



class BasketItemSerializer(ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['owner', 'electronic_book', 'audio_book', 'podcast', 'basket', 'created_at']
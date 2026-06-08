from django.urls import path
from basket.views import AddBasketItem, BasketItemList, DeleteBasketItem, DiscountAPIView



urlpatterns = [
    path('add-basket-item', AddBasketItem.as_view()),
    path('basket-item-list', BasketItemList.as_view()),
    path('delete-basket-item/<str:pk>', DeleteBasketItem.as_view()),
    path('discount/', DiscountAPIView.as_view()),
]
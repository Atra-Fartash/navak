from django.contrib import admin
from basket.models import Basket, BasketItem, Discount



class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'value', 'is_active']
    list_filter = ['discount_type', 'is_active']


admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Discount, DiscountAdmin)
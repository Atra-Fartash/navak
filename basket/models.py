from django.db import models
from django.contrib.auth.models import User
from product.models import AudioBook, ElectronicBook, Podcast
from django.utils import timezone



class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveBigIntegerField()
    discount = models.ForeignKey(to='Discount', on_delete=models.SET_NULL, null=True, blank=True)
    final_price = models.PositiveBigIntegerField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class BasketItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    electronic_book = models.ForeignKey(to=ElectronicBook, on_delete=models.CASCADE)
    audio_book = models.ForeignKey(to=AudioBook, on_delete=models.CASCADE)
    podcast = models.ForeignKey(to=Podcast, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Discount(models.Model):
    DISCOUNT_TYPE_CHOICES=[
        ('p', 'percent'),
        ('a', 'amount'),
    ]
    code = models.CharField(max_length=50)
    discount_type = models.CharField(max_length=1, choices=DISCOUNT_TYPE_CHOICES)
    value = models.PositiveIntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)   # Leave empty to make the code public
    is_single_use = models.BooleanField(default=False)                                      
    usage_count = models.PositiveIntegerField(default=0)   
    max_usage = models.PositiveIntegerField(default=1)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
    def is_valid_for_user(self, user):
        now = timezone.now()
        if not self.is_active:
            return False, 'This code is not active'
        
        if self.start_date > now or self.end_date < now:
            return False, 'This code is not active'
        
        if self.user and self.user!=user:
            return False, 'This code is not active'
        
        if self.is_single_use and self.usage_count > 1:
            return False, 'This code has already been used'
        
        if not self.is_single_use and self.usage_count >= self.max_usage:
            return False, 'The maximum usage limit for this code has been reached'
        
        return True, None
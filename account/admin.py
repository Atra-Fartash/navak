from django.contrib import admin
from account.models import Profile, Wallet, Transaction



admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Transaction)
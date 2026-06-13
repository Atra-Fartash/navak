from django.urls import path
from account.views import ProfileListCreate, ProfileRetrieveUpdateDestroy, TransactionView


urlpatterns = [
    path('profile-list-create', ProfileListCreate.as_view()),
    path('profile-retrieve-update-destroy', ProfileRetrieveUpdateDestroy.as_view()),
    path('transaction', TransactionView.as_view())
]
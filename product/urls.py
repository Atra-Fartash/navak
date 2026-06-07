from django.urls import path
from product.views import (ElectronicBookListCreate, ElectronicBookDestoryUpdateRetrieve, AudioBookListCreate,
                           AudioBookDestoryUpdateRetrieve,PodcastListCreate, PodcastDestoryUpdateRetrieve, CategoryListCreate,
                           CategoryDestoryUpdateRetrieve,PublisherListCreate, PublisherDestoryUpdateRetrieve, AuthorListCreate,
                           AuthorDestoryUpdateRetrieve,TranslatorListCreate, TranslatorDestoryUpdateRetrieve, NarratorListCreate,
                           NarratorDestoryUpdateRetrieve, CommentListCreate, CommentRetrieveUpdateDestroy)


urlpatterns = [
    path('electronic-book-list-create', ElectronicBookListCreate.as_view()),
    path('electronic-book-retrieve-update-destroy/<str:pk>', ElectronicBookDestoryUpdateRetrieve.as_view()),
    path('audio-book-list-create', AudioBookListCreate.as_view()),
    path('audio-book-retrieve-update-destroy/<str:pk>', AudioBookDestoryUpdateRetrieve.as_view()),
    path('podcast-list-create', PodcastListCreate.as_view()),
    path('podcast-retrieve-update-destroy/<str:pk>', PodcastDestoryUpdateRetrieve.as_view()),
    path('category-list-create', CategoryListCreate.as_view()),
    path('category-retrieve-update-destroy/<str:pk>', CategoryDestoryUpdateRetrieve.as_view()),
    path('publisher-list-create', PublisherListCreate.as_view()),
    path('publisher-retrieve-update-destroy/<str:pk>', PublisherDestoryUpdateRetrieve.as_view()),
    path('author-list-create', AuthorListCreate.as_view()),
    path('author-retrieve-update-destroy/<str:pk>', AuthorDestoryUpdateRetrieve.as_view()),
    path('translator-list-create', TranslatorListCreate.as_view()),
    path('translator-retrieve-update-destroy/<str:pk>', TranslatorDestoryUpdateRetrieve.as_view()),
    path('narrator-list-create', NarratorListCreate.as_view()),
    path('narrator-retrieve-update-destroy/<str:pk>', NarratorDestoryUpdateRetrieve.as_view()),
    path('comment-list-create', CommentListCreate.as_view()),
    path('comment-retrieve-update-destroy/<str:pk>', CommentRetrieveUpdateDestroy.as_view()),
]
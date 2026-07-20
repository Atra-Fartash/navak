from product.models import (Category, Publisher, Author, Narrator,Translator,
                            AudioBook, ElectronicBook, Podcast, Comment)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.serializers import (CategorySerializer,CategoryRetrieveUpdateDestroySerializer, PublisherSerializer,
                                PublisherRetrieveUpdateDestroySerializer, AuthorSerializer,AuthorRetrieveUpdateDestroySerializer,
                                NarratorSerializer,NarratorRetrieveUpdateDestroySerializer, TranslatorSerializer,TranslatorRetrieveUpdateDestroySerializer,
                                AudioBookSerializer,AudioBookRetrieveUpdateDestroySerializer, ElectronicBookSerializer,ElectronicBookRetrieveUpdateDestroySerializer,
                                PodcastSerializer,PodcastRetrieveUpdateDestroySerializer, CommentSerializer, CommentRetrieveUpdateDestroySerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import permissions
from django.shortcuts import render



class ElectronicBookListCreate(ListCreateAPIView):
    queryset = ElectronicBook.objects.all()
    serializer_class = ElectronicBookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['price', 'score', 'page']


class ElectronicBookDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = ElectronicBook.objects.all()
    serializer_class = ElectronicBookRetrieveUpdateDestroySerializer
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['price', 'score', 'page']


class AudioBookListCreate(ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['price', 'score', 'time']


class AudioBookDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookRetrieveUpdateDestroySerializer
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['price', 'score', 'time']


class PodcastListCreate(ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['price', 'score', 'time']


class PodcastDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastRetrieveUpdateDestroySerializer
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['price', 'score', 'time']


class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']


class CategoryDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']


class PublisherListCreate(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class PublisherDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class AuthorListCreate(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class AuthorDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class TranslatorListCreate(ListCreateAPIView):
    queryset = Translator.objects.all()
    serializer_class = TranslatorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class TranslatorDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Translator.objects.all()
    serializer_class = TranslatorRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class NarratorListCreate(ListCreateAPIView):
    queryset = Narrator.objects.all()
    serializer_class = NarratorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class NarratorDestoryUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Narrator.objects.all()
    serializer_class = NarratorRetrieveUpdateDestroySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class CommentListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(user=user)


def product_detail(request):
    electronic_books = ElectronicBook.objects.all()
    audio_books = AudioBook.objects.all()
    podcast = Podcast.objects.all()
    data = {
        'electronic_books' : electronic_books,
        'audio_books' :  audio_books,
        'podcast' : podcast
    }
    return render(request, 'product-detail.html', context=data)

def products(request):
    electronic_books = ElectronicBook.objects.all()
    audio_books = AudioBook.objects.all()
    podcast = Podcast.objects.all()
    data = {
        'electronic_books' : electronic_books,
        'audio_books' :  audio_books,
        'podcast' : podcast
    }
    return render(request, 'products.html', context=data)


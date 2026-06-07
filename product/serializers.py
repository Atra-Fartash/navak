from product.models import Category, Publisher, Author, Narrator, Translator, AudioBook, ElectronicBook, Podcast, Comment
from rest_framework.serializers import ModelSerializer



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class CategoryRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'description']


class PublisherRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'description']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'biography', 'picture']


class AuthorRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'biography', 'picture']


class NarratorSerializer(ModelSerializer):
    class Meta:
        model = Narrator
        fields = ['name', 'biography', 'picture']


class NarratorRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Narrator
        fields = ['name', 'biography', 'picture']


class TranslatorSerializer(ModelSerializer):
    class Meta:
        model = Translator
        fields = ['name', 'biography', 'picture']


class TranslatorRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Translator
        fields = ['name', 'biography', 'picture']


class AudioBookSerializer(ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['name', 'category', 'user', 'picture', 'author', 'narrator','translator',
                   'publications', 'score', 'description', 'price', 'time', 'audio_book']
        

class AudioBookRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['name', 'category', 'user', 'picture', 'author', 'narrator','translator',
                   'publications', 'score', 'description', 'price', 'time', 'audio_book']


class ElectronicBookSerializer(ModelSerializer):
    class Meta:
        model = ElectronicBook
        fields = ['name', 'category', 'user', 'picture', 'author', 'translator',
                   'publisher', 'score', 'description', 'price', 'page', 'electronic_book']  
        

class ElectronicBookRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = ElectronicBook
        fields = ['name', 'category', 'user', 'picture', 'author', 'translator',
                   'publisher', 'score', 'description', 'price', 'page', 'electronic_book'] 


class PodcastSerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['name', 'category', 'user', 'picture', 'narrator','score',
                   'description', 'price', 'time','episodes', 'podcast']    


class PodcastRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['name', 'category', 'user', 'picture', 'narrator','score',
                   'description', 'price', 'time','episodes', 'podcast'] 


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'date', 'text', 'podcast', 'audio_book', 'electronic_book'] 


class CommentRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'date', 'text', 'podcast', 'audio_book', 'electronic_book'] 
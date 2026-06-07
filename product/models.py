from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name 
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Narrator(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Translator(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class AudioBook(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(to= Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    narrator = models.ForeignKey(to=Narrator, on_delete=models.CASCADE)
    translator = models.ForeignKey(to=Translator, on_delete=models.CASCADE)
    publications = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    time = models.DurationField()
    audio_book = models.FileField(null=True, blank=True)


class ElectronicBook(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(to= Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    translator = models.ForeignKey(to=Translator, on_delete=models.CASCADE)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    page = models.PositiveIntegerField()
    electronic_book = models.FileField(null=True, blank=True)


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(to= Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True)
    narrator = models.ForeignKey(to=Narrator, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    time = models.DurationField()
    episodes = models.PositiveIntegerField()
    podcast = models.FileField(null=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
    podcast = models.ForeignKey(to=Podcast, on_delete=models.CASCADE, null=True, blank=True)
    audio_book = models.ForeignKey(to=AudioBook, on_delete=models.CASCADE, null=True, blank=True)
    electronic_book = models.ForeignKey(to=ElectronicBook, on_delete=models.CASCADE, null=True, blank=True)

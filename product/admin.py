from django.contrib import admin
from product.models import Category, Publisher, Author, Narrator, Translator, AudioBook, ElectronicBook, Podcast, Comment


class AudioBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    search_fields = ['name']
    list_filter = ['category', 'price']

class ElectronicBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    search_fields = ['name']
    list_filter = ['category', 'price']

class PodcastAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    search_fields = ['name']
    list_filter = ['category', 'price']

admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Narrator)
admin.site.register(Translator)
admin.site.register(AudioBook, AudioBookAdmin)
admin.site.register(ElectronicBook, ElectronicBookAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Comment)
from django.contrib import admin
from .models import Author, Genre, Book, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_year', 'books_count', 'created_at']
    search_fields = ['name', 'bio']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = 'Books'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'books_count']
    search_fields = ['name']

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = 'Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year', 'average_rating', 'ratings_count', 'created_at']
    list_filter = ['genres', 'language', 'published_year', 'created_at']
    search_fields = ['title', 'author__name', 'isbn', 'publisher']
    filter_horizontal = ['genres']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user_name', 'comment', 'book__title']
    readonly_fields = ['created_at']
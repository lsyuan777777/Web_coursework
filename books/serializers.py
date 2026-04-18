from rest_framework import serializers
from .models import Author, Genre, Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'user_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']


class GenreSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'books_count', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_books_count(self, obj):
        return obj.books.count()


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_year', 'books_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_books_count(self, obj):
        return obj.books.count()


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_year', 'books', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_books(self, obj):
        books = obj.books.all()[:10]
        return BookListSerializer(books, many=True).data


class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    genres_list = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author_name', 'genres_list', 'isbn',
            'published_year', 'average_rating', 'ratings_count',
            'page_count', 'language', 'image_url', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_genres_list(self, obj):
        return list(obj.genres.values_list('name', flat=True))


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'genres', 'isbn', 'published_year',
            'description', 'average_rating', 'ratings_count', 'page_count',
            'language', 'publisher', 'image_url', 'reviews', 'reviews_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_reviews(self, obj):
        reviews = obj.reviews.all()[:5]
        return ReviewSerializer(reviews, many=True).data


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, source='genres', write_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author_id', 'genre_ids', 'isbn', 'published_year',
            'description', 'average_rating', 'ratings_count', 'page_count',
            'language', 'publisher', 'image_url'
        ]

    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        genre_ids = validated_data.pop('genres', [])
        book = Book.objects.create(author=author_id, **validated_data)
        for genre in genre_ids:
            book.genres.add(genre)
        return book

    def update(self, instance, validated_data):
        author_id = validated_data.pop('author_id', None)
        genre_ids = validated_data.pop('genres', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if author_id is not None:
            instance.author = author_id

        instance.save()

        if genre_ids is not None:
            instance.genres.clear()
            for genre in genre_ids:
                instance.genres.add(genre)

        return instance
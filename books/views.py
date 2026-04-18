from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg, Q
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Author, Genre, Book, Review
from .serializers import (
    AuthorSerializer, AuthorDetailSerializer,
    GenreSerializer,
    BookListSerializer, BookDetailSerializer, BookCreateUpdateSerializer,
    ReviewSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'bio']
    ordering_fields = ['name', 'created_at', 'birth_year']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorSerializer

    @extend_schema(
        summary="List all authors with book counts",
        description="Returns a paginated list of authors, each with their book count."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get author details with recent books",
        description="Returns detailed information about a specific author including their books."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = None

    @extend_schema(
        summary="List all genres",
        description="Returns a list of all book genres with book counts."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').prefetch_related('genres', 'reviews').all()
    serializer_class = BookListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name', 'isbn', 'publisher']
    ordering_fields = ['title', 'published_year', 'average_rating', 'ratings_count', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookCreateUpdateSerializer
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookListSerializer

    @extend_schema(
        summary="List all books",
        description="Returns a paginated list of books with basic information."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get book details",
        description="Returns detailed information about a specific book including reviews."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new book",
        description="Creates a new book with the specified details."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Update a book",
        description="Updates an existing book's details."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a book",
        description="Deletes a book from the database."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="Get books by genre",
        description="Returns books filtered by a specific genre.",
        parameters=[
            OpenApiParameter(name='genre_id', description='Genre ID', required=True, type=int)
        ]
    )
    @action(detail=False, methods=['get'])
    def by_genre(self, request):
        genre_id = request.query_params.get('genre_id')
        if not genre_id:
            return Response(
                {'error': 'genre_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        books = self.queryset.filter(genres__id=genre_id)
        page = self.paginate_queryset(books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Get top rated books",
        description="Returns the top rated books sorted by average rating.",
        parameters=[
            OpenApiParameter(name='limit', description='Number of books to return', required=False, type=int)
        ]
    )
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        limit = int(request.query_params.get('limit', 10))
        books = self.queryset.filter(
            average_rating__isnull=False
        ).order_by('-average_rating')[:limit]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Search books by title or author",
        description="Full-text search across book titles and author names.",
        parameters=[
            OpenApiParameter(name='q', description='Search query', required=True, type=str)
        ]
    )
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response(
                {'error': 'Search query (q) is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        books = self.queryset.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
        page = self.paginate_queryset(books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('book').all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        book_id = self.request.query_params.get('book_id')
        if book_id:
            queryset = queryset.filter(book_id=book_id)
        return queryset

    @extend_schema(
        summary="List all reviews",
        description="Returns all reviews, optionally filtered by book_id."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get review details",
        description="Returns detailed information about a specific review."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new review",
        description="Creates a new review for a book."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Update a review",
        description="Updates an existing review."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a review",
        description="Deletes a review from the database."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AnalyticsViewSet(viewsets.ViewSet):
    @extend_schema(
        summary="Get genre distribution",
        description="Returns the number of books per genre."
    )
    @action(detail=False, methods=['get'])
    def genre_distribution(self, request):
        genres = Genre.objects.annotate(
            book_count=Count('books')
        ).order_by('-book_count')
        data = [{'id': g.id, 'name': g.name, 'book_count': g.book_count} for g in genres]
        return Response(data)

    @extend_schema(
        summary="Get rating distribution",
        description="Returns the distribution of book ratings."
    )
    @action(detail=False, methods=['get'])
    def rating_distribution(self, request):
        distribution = {
            '5_stars': Book.objects.filter(average_rating__gte=4.5).count(),
            '4_stars': Book.objects.filter(average_rating__gte=4.0, average_rating__lt=4.5).count(),
            '3_stars': Book.objects.filter(average_rating__gte=3.0, average_rating__lt=4.0).count(),
            '2_stars': Book.objects.filter(average_rating__gte=2.0, average_rating__lt=3.0).count(),
            '1_star': Book.objects.filter(average_rating__gte=1.0, average_rating__lt=2.0).count(),
        }
        return Response(distribution)

    @extend_schema(
        summary="Get yearly publication stats",
        description="Returns statistics of books published per year."
    )
    @action(detail=False, methods=['get'])
    def yearly_stats(self, request):
        from django.db.models.functions import ExtractYear
        stats = Book.objects.exclude(
            published_year__isnull=True
        ).annotate(
            year=ExtractYear('published_year')
        ).values('year').annotate(
            count=Count('id')
        ).order_by('-year')[:20]
        return Response(list(stats))

    @extend_schema(
        summary="Get dashboard summary",
        description="Returns overall statistics for the API."
    )
    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        total_books = Book.objects.count()
        total_authors = Author.objects.count()
        total_reviews = Review.objects.count()
        total_genres = Genre.objects.count()
        avg_rating = Book.objects.aggregate(Avg('average_rating'))['average_rating__avg']
        return Response({
            'total_books': total_books,
            'total_authors': total_authors,
            'total_reviews': total_reviews,
            'total_genres': total_genres,
            'average_rating': round(avg_rating, 2) if avg_rating else None
        })
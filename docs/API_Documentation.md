# Books API - Technical Documentation

## Overview

This document provides comprehensive API documentation for the Books Metadata and Recommendation API. The API is built using Django REST Framework and provides full CRUD operations for managing books, authors, genres, and reviews.

**Base URL**: `http://127.0.0.1:8000/api/`

---

## Authentication

This API does not currently require authentication. All endpoints are publicly accessible.

---

## API Endpoints

### Authors

#### List All Authors
```
GET /api/authors/
```

**Response**:
```json
{
  "count": 8,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "J.R.R. Tolkien",
      "bio": "British writer...",
      "birth_year": 1892,
      "books_count": 2,
      "created_at": "2026-04-14T03:54:38Z",
      "updated_at": "2026-04-14T03:54:38Z"
    }
  ]
}
```

#### Get Author Details
```
GET /api/authors/{id}/
```

**Response**:
```json
{
  "id": 1,
  "name": "J.R.R. Tolkien",
  "bio": "British writer...",
  "birth_year": 1892,
  "books": [...],
  "created_at": "2026-04-14T03:54:38Z",
  "updated_at": "2026-04-14T03:54:38Z"
}
```

#### Create Author
```
POST /api/authors/
```

**Request Body**:
```json
{
  "name": "New Author",
  "bio": "Author biography",
  "birth_year": 1970
}
```

#### Update Author
```
PUT /api/authors/{id}/
```

#### Delete Author
```
DELETE /api/authors/{id}/
```

**Query Parameters**:
- `search`: Search by name or bio
- `ordering`: Order by name, created_at, or birth_year

---

### Books

#### List All Books
```
GET /api/books/
```

**Response**:
```json
{
  "count": 15,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "The Hobbit",
      "author_name": "J.R.R. Tolkien",
      "genres_list": ["Fantasy"],
      "isbn": "978-0547928227",
      "published_year": 1937,
      "average_rating": "4.70",
      "ratings_count": 2000,
      "page_count": 310,
      "language": "English",
      "image_url": null,
      "created_at": "2026-04-14T03:54:38Z"
    }
  ]
}
```

#### Get Book Details
```
GET /api/books/{id}/
```

**Response**:
```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": {...},
  "genres": [...],
  "isbn": "978-0547928227",
  "published_year": 1937,
  "description": "The story of Bilbo Baggins...",
  "average_rating": "4.70",
  "ratings_count": 2000,
  "page_count": 310,
  "language": "English",
  "publisher": null,
  "image_url": null,
  "reviews": [...],
  "reviews_count": 1,
  "created_at": "2026-04-14T03:54:38Z",
  "updated_at": "2026-04-14T03:54:38Z"
}
```

#### Create Book
```
POST /api/books/
```

**Request Body**:
```json
{
  "title": "New Book",
  "author_id": 1,
  "genre_ids": [1, 2],
  "isbn": "978-1234567890",
  "published_year": 2024,
  "description": "Book description",
  "average_rating": 4.5,
  "ratings_count": 100,
  "page_count": 300,
  "language": "English",
  "publisher": "Publisher Name"
}
```

#### Update Book
```
PUT /api/books/{id}/
```

#### Delete Book
```
DELETE /api/books/{id}/
```

#### Get Top Rated Books
```
GET /api/books/top_rated/?limit=10
```

**Query Parameters**:
- `limit`: Number of books to return (default: 10)

#### Get Books by Genre
```
GET /api/books/by_genre/?genre_id=1
```

**Query Parameters**:
- `genre_id`: Genre ID (required)

#### Search Books
```
GET /api/books/search/?q=tolkien
```

**Query Parameters**:
- `q`: Search query (required)

**General Query Parameters**:
- `search`: Search by title, author, ISBN, or publisher
- `ordering`: Order by title, published_year, average_rating, ratings_count, or created_at

---

### Genres

#### List All Genres
```
GET /api/genres/
```

**Response**:
```json
[
  {
    "id": 1,
    "name": "Fantasy",
    "description": "Books with magical elements...",
    "books_count": 6,
    "created_at": "2026-04-14T03:54:38Z"
  }
]
```

#### Get Genre Details
```
GET /api/genres/{id}/
```

#### Create Genre
```
POST /api/genres/
```

**Request Body**:
```json
{
  "name": "Science Fiction",
  "description": "Speculative fiction..."
}
```

#### Update Genre
```
PUT /api/genres/{id}/
```

#### Delete Genre
```
DELETE /api/genres/{id}/
```

---

### Reviews

#### List All Reviews
```
GET /api/reviews/
```

#### Filter Reviews by Book
```
GET /api/reviews/?book_id=1
```

**Query Parameters**:
- `book_id`: Filter by book ID

#### Get Review Details
```
GET /api/reviews/{id}/
```

#### Create Review
```
POST /api/reviews/
```

**Request Body**:
```json
{
  "book": 1,
  "user_name": "John",
  "rating": 5,
  "comment": "Great book!"
}
```

#### Update Review
```
PUT /api/reviews/{id}/
```

#### Delete Review
```
DELETE /api/reviews/{id}/
```

---

### Analytics

#### Get Dashboard Summary
```
GET /api/analytics/dashboard/
```

**Response**:
```json
{
  "total_books": 15,
  "total_authors": 8,
  "total_reviews": 9,
  "total_genres": 6,
  "average_rating": 4.44
}
```

#### Get Genre Distribution
```
GET /api/analytics/genre_distribution/
```

**Response**:
```json
[
  {"id": 1, "name": "Fantasy", "book_count": 6},
  {"id": 2, "name": "Science Fiction", "book_count": 4},
  ...
]
```

#### Get Rating Distribution
```
GET /api/analytics/rating_distribution/
```

**Response**:
```json
{
  "5_stars": 3,
  "4_stars": 5,
  "3_stars": 2,
  "2_stars": 0,
  "1_star": 0
}
```

#### Get Yearly Statistics
```
GET /api/analytics/yearly_stats/
```

**Response**:
```json
[
  {"year": 1986, "count": 1},
  {"year": 1977, "count": 1},
  ...
]
```

---

## Error Codes

The API uses standard HTTP status codes:

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 204 | No Content - Resource deleted successfully |
| 400 | Bad Request - Invalid input data |
| 404 | Not Found - Resource not found |
| 500 | Internal Server Error - Server-side error |

**Error Response Format**:
```json
{
  "field_name": ["Error message"]
}
```

---

## Pagination

List endpoints use pagination with the following format:
```json
{
  "count": 15,
  "next": "http://127.0.0.1:8000/api/books/?page=2",
  "previous": null,
  "results": [...]
}
```

Default page size is 20, configurable via `REST_FRAMEWORK.PAGE_SIZE` in settings.

---

## Data Validation

- **Author name**: Max 200 characters
- **Book title**: Max 300 characters
- **ISBN**: 13 characters, unique
- **Review rating**: 1-5 stars
- **Book rating**: 0-5 stars (decimal)
- **Published year**: Positive integer

---

## API Documentation URLs

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- ReDoc: `http://127.0.0.1:8000/api/redoc/`
- OpenAPI Schema: `http://127.0.0.1:8000/api/schema/`

---

## Testing Examples

### Using curl

```bash
# List all books
curl http://127.0.0.1:8000/api/books/

# Get book details
curl http://127.0.0.1:8000/api/books/1/

# Create a book
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"New Book","author_id":1,"genre_ids":[1]}'

# Get dashboard
curl http://127.0.0.1:8000/api/analytics/dashboard/
```

### Using Python requests

```python
import requests

# List all books
response = requests.get('http://127.0.0.1:8000/api/books/')
print(response.json())

# Create a book
data = {
    'title': 'New Book',
    'author_id': 1,
    'genre_ids': [1],
    'isbn': '978-1234567890',
    'published_year': 2024
}
response = requests.post('http://127.0.0.1:8000/api/books/', json=data)
print(response.status_code)
```

---

## Technology Stack

- **Framework**: Django 5.0.6
- **API**: Django REST Framework 3.15.1
- **Documentation**: drf-spectacular 0.27.1 (OpenAPI 3.0)
- **Database**: SQLite3
- **Server**: Gunicorn (production)

---

*Generated: April 2026*
*API Version: 1.0.0*
# Books API - Books Metadata & Recommendation Service

A comprehensive RESTful API for books metadata management, built with Django REST Framework. This API provides full CRUD operations for authors, genres, books, and reviews, along with analytics endpoints for insights into book trends and ratings.

## Project Overview

This project implements a complete web service API that manages a collection of books with their associated authors, genres, and reviews. The API includes advanced search capabilities, filtering, and analytical endpoints to provide insights into the book collection.

## Features

### Core Functionality
- **Complete CRUD Operations**: Create, Read, Update, Delete for all resources
- **Relational Data Model**: Authors, Books, Genres, and Reviews with proper relationships
- **Advanced Filtering**: Search by title, author name, genre, rating range, and more
- **Pagination**: PageNumberPagination with configurable page size

### API Endpoints

#### Authors
- `GET /api/authors/` - List all authors
- `GET /api/authors/{id}/` - Get author details with their books
- `POST /api/authors/` - Create a new author
- `PUT /api/authors/{id}/` - Update author
- `DELETE /api/authors/{id}/` - Delete author

#### Books
- `GET /api/books/` - List all books (with optional search and ordering)
- `GET /api/books/{id}/` - Get book details with reviews
- `POST /api/books/` - Create a new book
- `PUT /api/books/{id}/` - Update book
- `DELETE /api/books/{id}/` - Delete book
- `GET /api/books/top_rated/?limit=10` - Get top-rated books
- `GET /api/books/by_genre/?genre_id=1` - Get books by genre
- `GET /api/books/search/?q=query` - Full-text search

#### Genres
- `GET /api/genres/` - List all genres with book counts
- `POST /api/genres/` - Create a new genre
- `GET /api/genres/{id}/` - Get genre details

#### Reviews
- `GET /api/reviews/` - List all reviews
- `GET /api/reviews/?book_id=1` - Filter reviews by book
- `POST /api/reviews/` - Submit a new review
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

#### Analytics (Bonus Advanced Features)
- `GET /api/analytics/dashboard/` - Overall statistics (book count, author count, avg rating)
- `GET /api/analytics/genre_distribution/` - Number of books per genre
- `GET /api/analytics/rating_distribution/` - Distribution of ratings (5-star, 4-star, etc.)
- `GET /api/analytics/yearly_stats/` - Books published per year

## Tech Stack & Design Justification

### Backend: Python + Django REST Framework
- **Django**: Mature, production-ready framework with excellent ORM
- **DRF**: Industry-standard for building REST APIs in Python, with built-in serialization, authentication, viewsets, and more
- **Decision**: Django was chosen for its robustness, comprehensive documentation, built-in admin interface, and ORM's powerful query capabilities. DRF provides excellent API development speed while maintaining quality

### Database: SQLite3
- **SQLite**: Lightweight, file-based database, perfect for development and small to medium applications
- **Production**: Easily scalable to PostgreSQL or MySQL
- **Decision**: SQLite chosen for simplicity and zero-configuration deployment. The relational model fits the domain perfectly (books, authors, genres, reviews)

### API Documentation: drf-spectacular (OpenAPI/Swagger)
- **drf-spectacular**: Modern OpenAPI 3 schema generation for DRF
- **Features**: Auto-generated interactive API docs, schema validation
- **Decision**: Provides excellent automatic documentation with minimal configuration, supports modern OpenAPI standards

### Additional Libraries
- `django-cors-headers`: Enables CORS for frontend integration
- `gunicorn`: Production-ready WSGI server
- `python-dotenv`: Environment variable management

## Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd books_api
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python manage.py migrate
```

5. **Load sample data (optional)**
```bash
python seed_data.py
```

6. **Start the development server**
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

### API Documentation
- **Swagger UI**: `http://127.0.0.1:8000/api/schema/swagger-ui/`
- **ReDoc**: `http://127.0.0.1:8000/api/schema/redoc/`
- **OpenAPI JSON**: `http://127.0.0.1:8000/api/schema/`

## Project Structure

```
books_api/
├── books_api/          # Django project settings
│   ├── __init__.py
│   ├── settings.py     # Project configuration
│   ├── urls.py         # Root URL routing
│   └── wsgi.py         # WSGI application
├── books/              # Books app
│   ├── models.py       # Database models (Author, Genre, Book, Review)
│   ├── serializers.py  # DRF serializers for API representation
│   ├── views.py        # ViewSets and API endpoints
│   ├── urls.py         # App-level URL routing
│   ├── admin.py        # Django admin configuration
│   └── apps.py         # App configuration
├── static/             # Static files (CSS, JS)
├── media/              # User-uploaded media
├── manage.py           # Django CLI
├── requirements.txt    # Python dependencies
├── seed_data.py        # Sample data population script
└── README.md           # This file
```

## Version Control

This project uses Git for version control. All changes are committed with descriptive messages following conventional commit style:

```
feat: add new search endpoint for books
fix: correct pagination in analytics view
docs: update README with API documentation
```

## Testing

Tests can be run with:
```bash
python manage.py test books
```

### Testing Approach
- Unit tests for models and serializers
- API endpoint tests using DRF's test client
- Integration tests for complex queries and filters

## Deployment

The application can be deployed to various platforms:

### PythonAnywhere (Recommended for Assignment)
1. Upload the repository to GitHub
2. Create a new PythonAnywhere account
3. Set up a new web app with Python 3.9+
4. Clone the repository and install dependencies
5. Run migrations
6. Configure WSGI file
7. Set up static file serving

### Docker (Alternative)
A Dockerfile can be created for containerized deployment:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "books_api.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## API Error Handling

The API uses standard HTTP status codes:
- `200 OK`: Successful GET requests
- `201 Created`: Successful POST requests
- `204 No Content`: Successful DELETE requests
- `400 Bad Request`: Invalid input data
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server-side errors

## Data Validation

- Required fields are enforced at model level
- ISBN uniqueness constraint
- Rating validation (1-5 for reviews, 0-5 for book ratings)
- Year validation (positive integers)

## Future Enhancements

- User authentication and authorization (JWT tokens)
- Advanced recommendation algorithm based on user ratings
- Caching layer for frequently accessed data
- Rate limiting
- Export functionality (CSV, JSON)
- Image upload for book covers
- Webhook notifications for data changes
- Batch import/export
- GraphQL API alternative to REST

## Learning Outcomes & Reflection

This project demonstrates:
1. **Software Engineering Principles**: Clean separation of concerns, DRY code, RESTful design
2. **Database Design**: Proper relational modeling with foreign keys, many-to-many relationships
3. **API Design**: RESTful patterns, HTTP standards, proper status codes
4. **Documentation**: Self-documenting API with OpenAPI/Swagger
5. **Version Control**: Git workflow with meaningful commit messages
6. **Deployment**: Configurable for multiple platforms

## License

This project is created for academic purposes as part of the XJCO3011 module at the University of Leeds.

## Data Sources

Sample data is fictional and created for demonstration purposes. In a production scenario, this API could integrate with:
- Goodreads API
- Google Books API
- Open Library API
- ISBNdb API

## Contact

For questions about this project, please contact the module team:
- Dr Ammar Alsalka: M.A.Alsalka@leeds.ac.uk
- Mr Omar Choudhry: O.Choudhry@leeds.ac.uk
- Dr Guilin Zhao: G.Zhao@leeds.ac.uk
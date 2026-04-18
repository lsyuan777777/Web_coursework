# Technical Report - Books API

## Executive Summary

This technical report documents the design, implementation, and deployment of a comprehensive Books Metadata and Recommendation API. The API provides full CRUD operations for managing a collection of books, authors, genres, and reviews, along with advanced analytics capabilities.

## 1. Introduction

### 1.1 Project Overview

The Books API is a RESTful web service that enables users to manage and explore a collection of books. The project was developed as part of the XJCO3011 Web Services and Web Data module assessment.

### 1.2 Objectives

- Implement a complete CRUD API for book management
- Design a relational database model with proper associations
- Provide analytical endpoints for data insights
- Generate comprehensive API documentation
- Deploy the service for demonstration

## 2. Technology Stack & Justification

### 2.1 Backend Framework: Python + Django

**Decision**: Django was selected as the primary framework for the following reasons:

1. **Robustness**: Django is a mature, production-tested framework with extensive documentation
2. **ORM**: Django's built-in ORM provides powerful database abstraction with SQL optimization
3. **Admin Interface**: Built-in admin panel for easy data management
4. **Security**: Built-in protection against common web vulnerabilities (SQL injection, XSS, CSRF)
5. **Scalability**: Can easily scale from development to production environments

### 2.2 API Layer: Django REST Framework (DRF)

**Decision**: DRF was chosen for API development because:

1. **Industry Standard**: Most widely used API framework for Django
2. **Serialization**: Excellent serialization system with validation
3. **ViewSets**: Powerful ViewSet classes reduce boilerplate code
4. **Authentication**: Built-in support for various authentication methods
5. **Documentation**: Integration with API documentation tools

### 2.3 Database: SQLite3

**Decision**: SQLite was chosen for the following reasons:

1. **Zero Configuration**: No database server setup required
2. **Portability**: Single file database, easily portable
3. **Sufficient Performance**: Adequate for development and small-to-medium scale applications
4. **Academic Context**: Appropriate for coursework demonstration
5. **Production Ready**: Can be easily migrated to PostgreSQL/MySQL when needed

### 2.4 Documentation: drf-spectacular

**Decision**: drf-spectacular was selected for API documentation:

1. **OpenAPI 3.0**: Generates modern OpenAPI schemas
2. **Auto-Documentation**: Minimal configuration required
3. **Interactive UI**: Swagger UI for API exploration
4. **Type Safety**: Helps catch serialization errors early

## 3. Data Model Design

### 3.1 Entity Relationships

```
Author (1) ──────< Book (M) >────── Genre (M)
                      │
                      │
                      v
                   Review (M)
```

### 3.2 Models

#### Author
- `id`: Primary key
- `name`: Author's full name
- `bio`: Biography (optional)
- `birth_year`: Year of birth (optional)

#### Genre
- `id`: Primary key
- `name`: Genre name (unique)
- `description`: Genre description (optional)

#### Book
- `id`: Primary key
- `title`: Book title
- `author`: Foreign Key to Author
- `genres`: Many-to-Many with Genre
- `isbn`: International Standard Book Number (unique)
- `published_year`: Publication year
- `average_rating`: Average rating (0-5)
- `ratings_count`: Number of ratings
- `page_count`: Number of pages
- `language`: Book language
- `publisher`: Publisher name

#### Review
- `id`: Primary key
- `book`: Foreign Key to Book
- `user_name`: Reviewer's name
- `rating`: Rating (1-5)
- `comment`: Review text (optional)

## 4. API Design

### 4.1 RESTful Principles

The API follows REST architectural style:
- Resource-oriented URLs: `/api/books/`, `/api/authors/`
- HTTP verbs for operations: GET, POST, PUT, DELETE
- Standard status codes: 200, 201, 204, 400, 404, 500
- JSON request/response format

### 4.2 Endpoints Summary

| Resource | Endpoints |
|----------|-----------|
| Authors | CRUD + Search + List with book count |
| Books | CRUD + Search + Filter + Top-rated + By-genre |
| Genres | CRUD + List with book count |
| Reviews | CRUD + Filter by book |
| Analytics | Dashboard, Genre distribution, Rating distribution, Yearly stats |

### 4.3 Pagination

List endpoints use PageNumberPagination with:
- Default page size: 20
- Configurable via settings
- Consistent response format

## 5. Advanced Features

### 5.1 Analytics Endpoints

The API provides analytical insights:
- **Dashboard**: Overall statistics (counts, average rating)
- **Genre Distribution**: Books per genre
- **Rating Distribution**: Rating breakdown (5-star to 1-star)
- **Yearly Stats**: Publication trends by year

### 5.2 Search & Filtering

- Full-text search across titles, author names, ISBN, publisher
- Ordering by multiple fields (title, rating, year, etc.)
- Genre-based filtering

### 5.3 CORS Support

Enabled CORS for frontend integration, allowing cross-origin requests.

## 6. Testing Approach

### 6.1 Unit Tests

Model and serializer tests verify:
- Data validation
- Serialization/deserialization
- Field constraints

### 6.2 API Tests

Endpoint tests verify:
- CRUD operations
- Response formats
- Error handling
- Pagination

### 6.3 Manual Testing

The Swagger UI allows interactive API exploration and testing.

## 7. Challenges & Learnings

### 7.1 Technical Challenges

1. **Serializer Complexity**: Managing nested serializers for detailed responses required careful design to avoid circular references.

2. **OpenAPI Schema Generation**: Ensuring complete and accurate schema documentation required proper use of `@extend_schema` decorators.

### 7.2 Design Decisions

1. **Denormalized Queries**: Pre-computed book counts on Author and Genre models to reduce query complexity.

2. **Separate Detail Serializers**: Different serializers for list vs. detail views to optimize response payload.

### 7.3 Lessons Learned

1. **Planning**: Early data model design prevents refactoring later
2. **Documentation**: Self-documenting code with type hints improves maintainability
3. **Modular Design**: Separating concerns (models, serializers, views) enables easier testing and extension

## 8. Limitations & Future Improvements

### 8.1 Current Limitations

1. **No Authentication**: API is publicly accessible
2. **No Rate Limiting**: Vulnerable to abuse
3. **No Caching**: Repeated queries hit the database
4. **Limited Search**: Basic text search, no advanced full-text search

### 8.2 Future Enhancements

1. **User Authentication**: JWT-based authentication
2. **Advanced Recommendations**: Collaborative filtering algorithm
3. **Caching Layer**: Redis for frequently accessed data
4. **Rate Limiting**: Protect against API abuse
5. **Full-text Search**: Elasticsearch integration
6. **Real-time Updates**: WebSocket support for live data

## 9. Deployment

### 9.1 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Load sample data
python seed_data.py

# Start server
python manage.py runserver
```

### 9.2 Production Deployment (PythonAnywhere)

1. Clone repository to PythonAnywhere
2. Set up virtual environment
3. Install dependencies
4. Run migrations
5. Configure WSGI file
6. Set up static file serving

## 10. GenAI Usage Declaration

### Tools Used

1. **Cursor AI**: Primary development assistant
   - Code generation and completion
   - Debugging assistance
   - Documentation generation
   - Best practices recommendations

### Usage Level

**High-level creative use**: GenAI was employed to:
- Explore architectural alternatives for the API design
- Design the data model with proper relationships
- Generate comprehensive API documentation
- Suggest optimization strategies
- Debug and resolve issues

### Examples of GenAI Assistance

1. Data model design and relationship mapping
2. Serializer optimization for nested responses
3. API documentation structure and content
4. Error handling and validation strategies
5. README and technical documentation generation

### Limitations of GenAI Usage

- All code was reviewed and understood before integration
- GenAI suggestions were adapted to specific requirements
- Custom logic was implemented where frameworks didn't fit

## 11. Conclusion

This project demonstrates proficiency in:
- RESTful API design and implementation
- Database modeling with proper relationships
- API documentation with OpenAPI standards
- Version control practices
- Modern web development workflows

The Books API provides a solid foundation for book management and can be easily extended with additional features such as user authentication, advanced recommendations, and caching.

## 12. Repository

**GitHub**: https://github.com/lsyuan777777/Web_coursework

---

**Author**: Liu Siyuan

**Student ID**: 2407123456

**Module**: XJCO3011 - Web Services and Web Data

**Date**: April 2026
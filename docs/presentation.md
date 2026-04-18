# Books API - Presentation Slides

## Slide 1: Title Slide

**Books Metadata & Recommendation API**

- Module: XJCO3011 Web Services and Web Data
- Coursework 1: Individual API Development Project
- Student Name: [Your Name]
- Date: April 2026

---

## Slide 2: Project Overview

**What is the Books API?**

A comprehensive RESTful web service for managing books, authors, genres, and reviews.

**Key Features:**
- Full CRUD operations for all resources
- Advanced search and filtering
- Analytics and insights endpoints
- OpenAPI/Swagger documentation
- Production-ready architecture

**Technology Stack:**
- Django + Django REST Framework
- SQLite Database
- drf-spectacular for API docs

---

## Slide 3: System Architecture

```
┌─────────────┐
│   Client    │
│ (Browser/   │
│   App)      │
└──────┬──────┘
       │ HTTP/REST
       ▼
┌─────────────────┐
│ Django REST     │
│ Framework       │
│  - Viewsets     │
│  - Serializers  │
│  - Pagination   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Django ORM      │
│ - QuerySets     │
│ - Relationships │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  SQLite         │
│  Database       │
└─────────────────┘
```

---

## Slide 4: Data Model

**Entities & Relationships**

```
    ┌──────────┐         ┌──────────┐
    │  Author  │1───<    │   Book   │ >───M──┐
    └──────────┘         └──────────┘        │
                                                │ M
    ┌──────────┐         ┌──────────┐        │
    │  Genre   │M───<    │   Book   │ >───<M──┘
    └──────────┘         └──────────┘        │
                                                │
                              ┌──────────┐     │
                              │  Review  │ <───┘
                              └──────────┘
```

**Models:**
- Author: name, bio, birth_year
- Book: title, author, genres, ISBN, rating, etc.
- Genre: name, description
- Review: book, user, rating, comment

---

## Slide 5: API Endpoints

**Core Resources**

| Resource | Endpoints | Operations |
|----------|-----------|------------|
| **Books** | `/api/books/` | CRUD + Search + Top-rated + By-genre |
| **Authors** | `/api/authors/` | CRUD + Search |
| **Genres** | `/api/genres/` | CRUD + Book count |
| **Reviews** | `/api/reviews/` | CRUD + Filter by book |

**Bonus Analytics:**
- `/api/analytics/dashboard/` - Overall stats
- `/api/analytics/genre_distribution/` - Books per genre
- `/api/analytics/rating_distribution/` - Rating breakdown
- `/api/analytics/yearly_stats/` - Publication trends

---

## Slide 6: API Documentation

**Self-Documenting API**

```
Endpoint: GET /api/books/
```

Response (JSON):
```json
{
  "count": 15,
  "results": [
    {
      "id": 1,
      "title": "The Hobbit",
      "author_name": "J.R.R. Tolkien",
      "genres_list": ["Fantasy"],
      "average_rating": "4.70",
      "ratings_count": 2000
    }
  ]
}
```

**Interactive Documentation:**
- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`
- OpenAPI Schema: `/api/schema/`

---

## Slide 7: Version Control & Git Workflow

**Git Best Practices**

```
commit history:
├── feat: add analytics dashboard endpoint
├── feat: implement book search functionality
├── docs: update API documentation
├── fix: correct pagination in book list
└── init: project setup with Django
```

**Branching Strategy:**
- `main` branch: stable production-ready code
- Feature branches: `feature/analytics`, `feature/search`
- Descriptive commit messages following conventional commits

**Repository Structure:**
- Versioned source code
- Detailed README with setup instructions
- Sample data scripts
- Complete documentation

---

## Slide 8: Testing & Quality Assurance

**Testing Approach**

1. **Unit Tests**
   - Model validation
   - Serializer behavior
   - Custom methods

2. **Integration Tests**
   - API endpoint responses
   - CRUD operations
   - Error handling

3. **Manual Testing**
   - Swagger UI exploration
   - curl command testing
   - Postman collections

**Code Quality:**
- Type hints in serializers
- Clean separation of concerns
- DRY (Don't Repeat Yourself) principle
- Comprehensive error handling

---

## Slide 9: Deployment & Hosting

**Deployment Options**

**Development:**
```bash
python manage.py runserver
# API available at http://127.0.0.1:8000
```

**Production (PythonAnywhere / Heroku / AWS):**
```bash
gunicorn books_api.wsgi:application
```

**Environment Configuration:**
- SQLite (development) → PostgreSQL (production)
- DEBUG=True (development) → DEBUG=False (production)
- Static/media file serving
- CORS configuration

**Requirements:**
- Python 3.9+
- All dependencies in `requirements.txt`

---

## Slide 10: Advanced Features & Extensions

**Beyond Basic Requirements**

✓ Analytics Dashboard
✓ Top-rated books endpoint
✓ Genre-based filtering
✓ Full-text search
✓ Advanced filtering & ordering

**Future Enhancements:**
- User authentication (JWT)
- Recommendation engine
- Caching layer (Redis)
- Rate limiting
- GraphQL alternative
- Real-time notifications
- Batch import/export

---

## Slide 11: Challenges & Solutions

**Technical Challenges**

1. **Nested Serialization Complexity**
   - Solution: Separate list/detail serializers
   - Optimized database queries with `select_related` and `prefetch_related`

2. **OpenAPI Schema Accuracy**
   - Solution: Used `@extend_schema` decorators
   - Added explicit serializer classes

3. **Database Query Optimization**
   - Solution: Database indexes on frequently queried fields
   - Denormalized book counts on Author/Genre models

---

## Slide 12: GenAI Usage & Reflection

**AI-Assisted Development**

**Tools Used:**
- Cursor AI (Primary development assistant)
- ChatGPT for architecture discussions

**Usage Pattern (High-Level Creative):**
- Explored alternative data model designs
- Generated initial API documentation structure
- Debugged complex serializer issues
- Suggested optimization strategies

**Reflection:**
AI tools significantly accelerated development while maintaining code quality. The AI helped explore architectural alternatives and identify potential issues early.

---

## Slide 13: Lessons Learned

**Key Takeaways**

1. **Planning is Crucial**
   - Data model design upfront saves refactoring time

2. **Documentation Matters**
   - Self-documenting code with OpenAPI saves future effort

3. **API Design Principles**
   - RESTful patterns enable intuitive interfaces
   - Consistent response formats improve usability

4. **Modern Tooling**
   - Django + DRF provides excellent developer experience
   - drf-spectacular simplifies API documentation

---

## Slide 14: Demo & Live Testing

**Live Demo**

1. **Swagger UI Exploration**
   - Browse endpoints
   - Try out API calls

2. **Analytics Dashboard**
   - View overall statistics
   - Genre distribution charts

3. **Search & Filter**
   - Search by author name
   - Filter by genre
   - Top-rated books

**Command Line Testing:**
```bash
# List all books
curl http://localhost:8000/api/books/

# Get top 5 rated
curl http://localhost:8000/api/books/top_rated/?limit=5

# Dashboard stats
curl http://localhost:8000/api/analytics/dashboard/
```

---

## Slide 15: Conclusion & Q&A

**Summary**

- Fully functional REST API with complete CRUD operations
- Clean, modular code architecture
- Comprehensive documentation
- Analytics and advanced search features
- Ready for deployment

**Thank You!**

**Questions?**

---

**Contact:**
- GitHub: [your-repo-url]
- API Docs: `/api/docs/`
- Technical Report: `docs/Technical_Report.pdf`

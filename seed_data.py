import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_api.settings')
django.setup()

from books.models import Author, Genre, Book, Review
from datetime import datetime

# 清理现有数据
Book.objects.all().delete()
Author.objects.all().delete()
Genre.objects.all().delete()
Review.objects.all().delete()

print("Creating sample data...")

# 创建作者
authors = [
    Author(name="J.R.R. Tolkien", birth_year=1892,
           bio="British writer, poet, philologist, and academic, best known for The Hobbit and The Lord of the Rings."),
    Author(name="George R.R. Martin", birth_year=1948,
           bio="American novelist and short story writer, best known for the epic fantasy series A Song of Ice and Fire."),
    Author(name="Agatha Christie", birth_year=1890,
           bio="English writer known for her detective novels, short stories, and plays, particularly those featuring Hercule Poirot and Miss Marple."),
    Author(name="J.K. Rowling", birth_year=1965,
           bio="British author and philanthropist who wrote the Harry Potter fantasy series."),
    Author(name="Isaac Asimov", birth_year=1920,
           bio="American writer and professor of biochemistry, best known for his works of science fiction."),
    Author(name="Arthur C. Clarke", birth_year=1917,
           bio="British science fiction writer, inventor, and futurist, best known for 2001: A Space Odyssey."),
    Author(name="Douglas Adams", birth_year=1952,
           bio="English author, comic radio dramatist, and musician, best known for The Hitchhiker's Guide to the Galaxy."),
    Author(name="Stephen King", birth_year=1947,
           bio="American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels."),
]

for author in authors:
    author.save()
print(f"Created {len(authors)} authors")

# 创建类型
genres = [
    Genre(name="Fantasy", description="Books with magical elements, supernatural themes, and imaginary worlds."),
    Genre(name="Science Fiction", description="Speculative fiction dealing with imaginative concepts like advanced science and technology."),
    Genre(name="Mystery", description="Stories where the plot revolves around solving a puzzle, often a crime."),
    Genre(name="Thriller", description="Fiction characterized by suspense, excitement, and high stakes."),
    Genre(name="Romance", description="Fiction that focuses on romantic relationships."),
    Genre(name="Historical Fiction", description="Stories set in the past with attention to period details."),
]

for genre in genres:
    genre.save()
print(f"Created {len(genres)} genres")

# 创建书籍
books_data = [
    {
        "title": "The Hobbit",
        "author_name": "J.R.R. Tolkien",
        "isbn": "978-0547928227",
        "published_year": 1937,
        "genres": ["Fantasy"],
        "page_count": 310,
        "description": "The story of Bilbo Baggins, a hobbit who embarks on an unexpected adventure.",
        "average_rating": 4.7,
        "ratings_count": 2000
    },
    {
        "title": "The Fellowship of the Ring",
        "author_name": "J.R.R. Tolkien",
        "isbn": "978-0547928210",
        "published_year": 1954,
        "genres": ["Fantasy"],
        "page_count": 423,
        "description": "The first volume in The Lord of the Rings, following Frodo's journey.",
        "average_rating": 4.8,
        "ratings_count": 3500
    },
    {
        "title": "A Game of Thrones",
        "author_name": "George R.R. Martin",
        "isbn": "978-0553103540",
        "published_year": 1996,
        "genres": ["Fantasy", "Thriller"],
        "page_count": 694,
        "description": "The first novel in the A Song of Ice and Fire series.",
        "average_rating": 4.5,
        "ratings_count": 2800
    },
    {
        "title": "A Clash of Kings",
        "author_name": "George R.R. Martin",
        "isbn": "978-0553108194",
        "published_year": 1998,
        "genres": ["Fantasy", "Thriller"],
        "page_count": 768,
        "description": "The second novel in the series, continuing the struggle for the Iron Throne.",
        "average_rating": 4.4,
        "ratings_count": 2400
    },
    {
        "title": "Murder on the Orient Express",
        "author_name": "Agatha Christie",
        "isbn": "978-0062693662",
        "published_year": 1934,
        "genres": ["Mystery", "Thriller"],
        "page_count": 256,
        "description": "Detective Hercule Poirot investigates a murder on a luxury train.",
        "average_rating": 4.2,
        "ratings_count": 1800
    },
    {
        "title": "The Murder of Roger Ackroyd",
        "author_name": "Agatha Christie",
        "isbn": "978-0062073784",
        "published_year": 1926,
        "genres": ["Mystery"],
        "page_count": 296,
        "description": "A classic mystery featuring Hercule Poirot solving a complex case.",
        "average_rating": 4.4,
        "ratings_count": 1600
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author_name": "J.K. Rowling",
        "isbn": "978-0747532699",
        "published_year": 1997,
        "genres": ["Fantasy"],
        "page_count": 223,
        "description": "The first book in the Harry Potter series, introducing the young wizard.",
        "average_rating": 4.6,
        "ratings_count": 5000
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author_name": "J.K. Rowling",
        "isbn": "978-0747538486",
        "published_year": 1998,
        "genres": ["Fantasy"],
        "page_count": 251,
        "description": "Harry returns to Hogwarts for his second year and faces a hidden chamber.",
        "average_rating": 4.5,
        "ratings_count": 4200
    },
    {
        "title": "Foundation",
        "author_name": "Isaac Asimov",
        "isbn": "978-0553294385",
        "published_year": 1951,
        "genres": ["Science Fiction"],
        "page_count": 255,
        "description": "A mathematician predicts the fall of the Galactic Empire and works to shorten the ensuing dark age.",
        "average_rating": 4.5,
        "ratings_count": 1500
    },
    {
        "title": "I, Robot",
        "author_name": "Isaac Asimov",
        "isbn": "978-0553804483",
        "published_year": 1950,
        "genres": ["Science Fiction"],
        "page_count": 224,
        "description": "A collection of short stories about robots and their interaction with humans.",
        "average_rating": 4.3,
        "ratings_count": 1300
    },
    {
        "title": "2001: A Space Odyssey",
        "author_name": "Arthur C. Clarke",
        "isbn": "978-0451457999",
        "published_year": 1968,
        "genres": ["Science Fiction"],
        "page_count": 289,
        "description": "A masterpiece about human evolution, technology, and first contact.",
        "average_rating": 4.4,
        "ratings_count": 1200
    },
    {
        "title": "Rendezvous with Rama",
        "author_name": "Arthur C. Clarke",
        "isbn": "978-0553287899",
        "published_year": 1973,
        "genres": ["Science Fiction"],
        "page_count": 256,
        "description": "An enigmatic cylindrical spaceship enters the Solar System, and a team is sent to explore it.",
        "average_rating": 4.3,
        "ratings_count": 900
    },
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author_name": "Douglas Adams",
        "isbn": "978-0345391803",
        "published_year": 1979,
        "genres": ["Science Fiction", "Fantasy"],
        "page_count": 224,
        "description": "A comedic science fiction novel following Arthur Dent's adventures through space.",
        "average_rating": 4.4,
        "ratings_count": 2000
    },
    {
        "title": "The Shining",
        "author_name": "Stephen King",
        "isbn": "978-0307743657",
        "published_year": 1977,
        "genres": ["Thriller", "Fantasy"],
        "page_count": 447,
        "description": "A family's winter stay at a haunted hotel turns into a nightmare.",
        "average_rating": 4.5,
        "ratings_count": 2500
    },
    {
        "title": "It",
        "author_name": "Stephen King",
        "isbn": "978-1501142970",
        "published_year": 1986,
        "genres": ["Thriller", "Fantasy"],
        "page_count": 1138,
        "description": "A group of friends return to their hometown to confront a shape-shifting evil entity.",
        "average_rating": 4.3,
        "ratings_count": 1800
    },
]

for book_data in books_data:
    author = Author.objects.get(name=book_data['author_name'])
    book = Book(
        title=book_data['title'],
        author=author,
        isbn=book_data.get('isbn'),
        published_year=book_data.get('published_year'),
        description=book_data.get('description'),
        page_count=book_data.get('page_count'),
        average_rating=book_data.get('average_rating'),
        ratings_count=book_data.get('ratings_count', 0)
    )
    book.save()
    for genre_name in book_data['genres']:
        genre, _ = Genre.objects.get_or_create(name=genre_name)
        book.genres.add(genre)
    book.save()

print(f"Created {len(books_data)} books")

# 创建评论
reviews_data = [
    ("The Hobbit", "Alice", 5, "A timeless classic!"),
    ("The Hobbit", "Bob", 4, "Great adventure story."),
    ("A Game of Thrones", "Charlie", 5, "Epic fantasy at its best."),
    ("Murder on the Orient Express", "Diana", 5, "Clever plot twist!"),
    ("Harry Potter and the Philosopher's Stone", "Eve", 5, "Magical and wonderful."),
    ("Foundation", "Frank", 4, "Brilliant sci-fi concept."),
    ("2001: A Space Odyssey", "Grace", 4, "Mind-bending and visionary."),
    ("The Hitchhiker's Guide to the Galaxy", "Henry", 5, "Hilarious and profound."),
    ("The Shining", "Ivy", 5, "King's masterpiece."),
]

for book_title, user, rating, comment in reviews_data:
    try:
        book = Book.objects.get(title=book_title)
        Review.objects.create(book=book, user_name=user, rating=rating, comment=comment)
    except Book.DoesNotExist:
        print(f"Warning: Book '{book_title}' not found, skipping review")

print(f"Created {len(reviews_data)} reviews")

print("Sample data creation complete!")
print(f"\nYou can now run: python manage.py runserver")

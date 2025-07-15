#!/usr/bin/env python3
"""
Sample Data Script for Library Management System
Populates the database with sample books for testing and demonstration.
"""

import sys
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import SessionLocal, Book

def create_sample_books():
    """Create sample books in the database."""
    
    sample_books = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "978-0743273565",
            "genre": "Fiction",
            "publication_year": 1925,
            "description": "A story of decadence and excess, Gatsby explores the darker aspects of the Jazz Age."
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "978-0446310789",
            "genre": "Fiction",
            "publication_year": 1960,
            "description": "A powerful story of racial injustice and the loss of innocence in the American South."
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "978-0451524935",
            "genre": "Science Fiction",
            "publication_year": 1949,
            "description": "A dystopian novel about totalitarianism and the manipulation of truth and reality."
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "isbn": "978-0141439518",
            "genre": "Romance",
            "publication_year": 1813,
            "description": "A classic romance about the relationship between Elizabeth Bennet and Mr. Darcy."
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "isbn": "978-0547928241",
            "genre": "Fantasy",
            "publication_year": 1937,
            "description": "An epic fantasy adventure about Bilbo Baggins' journey with thirteen dwarves."
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "isbn": "978-0316769488",
            "genre": "Fiction",
            "publication_year": 1951,
            "description": "A coming-of-age story about teenage alienation and loss of innocence in post-World War II America."
        },
        {
            "title": "Lord of the Flies",
            "author": "William Golding",
            "isbn": "978-0399501487",
            "genre": "Fiction",
            "publication_year": 1954,
            "description": "A novel about the dark side of human nature, exploring what happens when civilization breaks down."
        },
        {
            "title": "Animal Farm",
            "author": "George Orwell",
            "isbn": "978-0451526342",
            "genre": "Fiction",
            "publication_year": 1945,
            "description": "An allegorical novella about the Russian Revolution and the rise of Stalinism."
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "isbn": "978-0062315007",
            "genre": "Fiction",
            "publication_year": 1988,
            "description": "A novel about following your dreams and listening to your heart."
        },
        {
            "title": "The Little Prince",
            "author": "Antoine de Saint-Exupéry",
            "isbn": "978-0156013987",
            "genre": "Children",
            "publication_year": 1943,
            "description": "A poetic tale about a young prince who visits various planets in space."
        },
        {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "isbn": "978-0060850524",
            "genre": "Science Fiction",
            "publication_year": 1932,
            "description": "A dystopian novel about a futuristic society controlled by technology and conditioning."
        },
        {
            "title": "The Kite Runner",
            "author": "Khaled Hosseini",
            "isbn": "978-1594631931",
            "genre": "Fiction",
            "publication_year": 2003,
            "description": "A powerful story of friendship, betrayal, and redemption set against the backdrop of Afghanistan."
        },
        {
            "title": "The Book Thief",
            "author": "Markus Zusak",
            "isbn": "978-0375842207",
            "genre": "Historical Fiction",
            "publication_year": 2005,
            "description": "A story about the power of words and reading, set in Nazi Germany."
        },
        {
            "title": "Life of Pi",
            "author": "Yann Martel",
            "isbn": "978-0156027328",
            "genre": "Fiction",
            "publication_year": 2001,
            "description": "A philosophical novel about survival, faith, and the nature of storytelling."
        },
        {
            "title": "The Hunger Games",
            "author": "Suzanne Collins",
            "isbn": "978-0439023481",
            "genre": "Young Adult",
            "publication_year": 2008,
            "description": "A dystopian novel about a televised battle to the death between teenagers."
        },
        {
            "title": "The Fault in Our Stars",
            "author": "John Green",
            "isbn": "978-0525478812",
            "genre": "Young Adult",
            "publication_year": 2012,
            "description": "A touching story about two teenagers who fall in love while dealing with cancer."
        },
        {
            "title": "Gone Girl",
            "author": "Gillian Flynn",
            "isbn": "978-0307588364",
            "genre": "Thriller",
            "publication_year": 2012,
            "description": "A psychological thriller about a woman who disappears on her fifth wedding anniversary."
        },
        {
            "title": "The Martian",
            "author": "Andy Weir",
            "isbn": "978-0553418026",
            "genre": "Science Fiction",
            "publication_year": 2011,
            "description": "A science fiction novel about an astronaut stranded on Mars who must find a way to survive."
        },
        {
            "title": "Educated",
            "author": "Tara Westover",
            "isbn": "978-0399590504",
            "genre": "Biography",
            "publication_year": 2018,
            "description": "A memoir about a woman who leaves her survivalist family and goes on to earn a PhD."
        }
    ]
    
    db = SessionLocal()
    try:
        # Check if books already exist
        existing_books = db.query(Book).count()
        if existing_books > 0:
            print(f"Database already contains {existing_books} books. Skipping sample data creation.")
            return
        
        # Create sample books
        for book_data in sample_books:
            book = Book(**book_data)
            db.add(book)
        
        db.commit()
        print(f"Successfully created {len(sample_books)} sample books!")
        print("\nSample books added:")
        for book in sample_books:
            print(f"- {book['title']} by {book['author']}")
            
    except Exception as e:
        print(f"Error creating sample books: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Creating sample books for Library Management System...")
    create_sample_books()
    print("\nSample data creation completed!") 
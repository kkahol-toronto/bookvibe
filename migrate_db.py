#!/usr/bin/env python3
"""
Database Migration Script for BookVibe
Adds description_audience column to existing books table.
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import SessionLocal, Book
from sqlalchemy import text

def migrate_database():
    """Add description_audience column to existing database."""
    
    db = SessionLocal()
    try:
        # Check if the column already exists
        result = db.execute(text("PRAGMA table_info(books)"))
        columns = [row[1] for row in result.fetchall()]
        
        if 'description_audience' not in columns:
            print("Adding description_audience column to books table...")
            db.execute(text("ALTER TABLE books ADD COLUMN description_audience VARCHAR"))
            db.commit()
            print("✅ Successfully added description_audience column!")
        else:
            print("✅ description_audience column already exists.")
            
        # Update existing books to have null description_audience
        books_without_audience = db.query(Book).filter(Book.description_audience.is_(None)).all()
        for book in books_without_audience:
            book.description_audience = None
        
        db.commit()
        print(f"✅ Updated {len(books_without_audience)} existing books.")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Running BookVibe database migration...")
    migrate_database()
    print("Migration completed!") 
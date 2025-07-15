from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime
import os
from dotenv import load_dotenv
from typing import Optional, List
import json

# Load environment variables
load_dotenv()

# Configure OpenAI
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-07-01-preview"
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

app = FastAPI(title="BookVibe - AI-Powered Library Management", version="1.0.0")

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, unique=True, index=True)
    genre = Column(String)
    publication_year = Column(Integer)
    description = Column(Text)
    description_audience = Column(String, nullable=True)  # Store which audience the description is for
    is_checked_out = Column(Boolean, default=False)
    checked_out_by = Column(String, nullable=True)
    checked_out_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    genre: str
    publication_year: int
    description: Optional[str] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    genre: Optional[str] = None
    publication_year: Optional[int] = None
    description: Optional[str] = None

class CheckoutRequest(BaseModel):
    borrower_name: str

class DescriptionRequest(BaseModel):
    audience: str
    book_id: int

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Templates
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return templates.TemplateResponse("index.html", {"request": request, "books": books})

@app.get("/add-book", response_class=HTMLResponse)
async def add_book_page(request: Request):
    return templates.TemplateResponse("add_book.html", {"request": request})

@app.post("/add-book")
async def add_book(
    title: str = Form(...),
    author: str = Form(...),
    isbn: str = Form(...),
    genre: str = Form(...),
    publication_year: int = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db)
):
    book = Book(
        title=title,
        author=author,
        isbn=isbn,
        genre=genre,
        publication_year=publication_year,
        description=description
    )
    db.add(book)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit-book/{book_id}", response_class=HTMLResponse)
async def edit_book_page(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return templates.TemplateResponse("edit_book.html", {"request": request, "book": book})

@app.post("/edit-book/{book_id}")
async def edit_book(
    book_id: int,
    title: str = Form(...),
    author: str = Form(...),
    isbn: str = Form(...),
    genre: str = Form(...),
    publication_year: int = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = title
    book.author = author
    book.isbn = isbn
    book.genre = genre
    book.publication_year = publication_year
    book.description = description
    book.updated_at = datetime.utcnow()
    
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-book/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/checkout/{book_id}")
async def checkout_book(
    book_id: int,
    borrower_name: str = Form(...),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.is_checked_out:
        raise HTTPException(status_code=400, detail="Book is already checked out")
    
    book.is_checked_out = True
    book.checked_out_by = borrower_name
    book.checked_out_date = datetime.utcnow()
    db.commit()
    
    return RedirectResponse(url="/", status_code=303)

@app.post("/checkin/{book_id}")
async def checkin_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if not book.is_checked_out:
        raise HTTPException(status_code=400, detail="Book is not checked out")
    
    book.is_checked_out = False
    book.checked_out_by = None
    book.checked_out_date = None
    db.commit()
    
    return RedirectResponse(url="/", status_code=303)

@app.get("/search", response_class=HTMLResponse)
async def search_books(
    request: Request,
    q: str = "",
    db: Session = Depends(get_db)
):
    if q:
        books = db.query(Book).filter(
            (Book.title.contains(q)) |
            (Book.author.contains(q)) |
            (Book.isbn.contains(q)) |
            (Book.genre.contains(q))
        ).all()
    else:
        books = []
    
    return templates.TemplateResponse("search.html", {"request": request, "books": books, "query": q})

@app.get("/generate-descriptions", response_class=HTMLResponse)
async def generate_descriptions_page(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return templates.TemplateResponse("generate_descriptions.html", {"request": request, "books": books})

@app.post("/generate-description")
async def generate_description(
    book_id: int = Form(...),
    audience: str = Form(...),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Audience descriptions
    audience_descriptions = {
        "genz": "Generation Z (ages 9-24) - Digital natives who value authenticity, social justice, and quick, engaging content",
        "millennials": "Millennials (ages 25-40) - Tech-savvy adults who appreciate meaningful experiences and work-life balance",
        "genx": "Generation X (ages 41-56) - Independent, resourceful adults who value practicality and authenticity",
        "baby_boomers": "Baby Boomers (ages 57-75) - Traditional values, prefer detailed information and established authority",
        "silent_generation": "Silent Generation (ages 76+) - Respectful of tradition, value clear, respectful communication"
    }
    
    audience_desc = audience_descriptions.get(audience, "general audience")
    
    try:
        prompt = f"""
        Write a compelling book description for "{book.title}" by {book.author} (published in {book.publication_year}, genre: {book.genre}).
        
        Target audience: {audience_desc}
        
        The description should be:
        - Engaging and appropriate for the target audience
        - 2-3 sentences long
        - Highlight the most appealing aspects for this demographic
        - Use language and tone that resonates with this age group
        
        Current description: {book.description or 'No description available'}
        
        Generate a new description that would appeal to {audience}:
        """
        
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a skilled librarian who writes engaging book descriptions tailored to different audiences."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        generated_description = response.choices[0].message.content.strip()
        
        # Update the book with the new description and audience
        book.description = generated_description
        book.description_audience = audience
        book.updated_at = datetime.utcnow()
        db.commit()
        
        return {"success": True, "description": generated_description, "audience": audience}
        
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/book/{book_id}", response_class=HTMLResponse)
async def view_book_details(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Get all books with the same title and author (different audience descriptions)
    related_books = db.query(Book).filter(
        Book.title == book.title,
        Book.author == book.author,
        Book.description_audience.isnot(None)
    ).all()
    
    descriptions = []
    for b in related_books:
        if b.description and b.description_audience:
            descriptions.append({
                "audience": b.description_audience,
                "description": b.description,
                "generated_at": b.updated_at
            })
    
    return templates.TemplateResponse("book_details.html", {
        "request": request, 
        "book": book, 
        "descriptions": descriptions
    })

@app.get("/api/books")
async def get_books_api(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "genre": book.genre,
            "publication_year": book.publication_year,
            "description": book.description,
            "description_audience": book.description_audience,
            "is_checked_out": book.is_checked_out,
            "checked_out_by": book.checked_out_by,
            "checked_out_date": book.checked_out_date.isoformat() if book.checked_out_date else None
        }
        for book in books
    ]

@app.get("/api/book/{book_id}/descriptions")
async def get_book_descriptions(book_id: int, db: Session = Depends(get_db)):
    """Get all descriptions for a specific book"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Get all books with the same title and author (different audience descriptions)
    related_books = db.query(Book).filter(
        Book.title == book.title,
        Book.author == book.author,
        Book.description_audience.isnot(None)
    ).all()
    
    descriptions = []
    for b in related_books:
        if b.description and b.description_audience:
            descriptions.append({
                "audience": b.description_audience,
                "description": b.description,
                "generated_at": b.updated_at.isoformat() if b.updated_at else None
            })
    
    return {
        "book_id": book_id,
        "title": book.title,
        "author": book.author,
        "descriptions": descriptions
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
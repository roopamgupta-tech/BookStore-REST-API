# Import required FastAPI components
from fastapi import APIRouter, HTTPException

# Import Pydantic schemas for request and response validation
from app.schemas import (
    BookCreate,
    BookUpdate,
    BookResponse,
    BookDeleteResponse
)

# Create a router to organize all book-related endpoints
router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# Temporary in-memory storage for book records
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John",
        "price": 299
    },
    {
        "id": 2,
        "title": "Learn FastAPI",
        "author": "David",
        "price": 499
    }
]



# Retrieve all books with optional title and author filtering
@router.get("/", response_model=list[BookResponse])
async def get_books(
    title: str | None = None,
    author: str | None = None
):
    filtered_books = books

    if title:
        filtered_books = [
            book for book in filtered_books
            if title.lower() in book["title"].lower()
        ]

    if author:
        filtered_books = [
            book for book in filtered_books
            if author.lower() in book["author"].lower()
        ]

    return filtered_books



# Retrieve a single book using its unique ID
@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# Create a new book and automatically generate its unique ID
@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate):
    new_book = {
        "id": max((b["id"] for b in books), default=0) + 1,
        **book.model_dump()
    }

    books.append(new_book)
    return new_book



# Update an existing book using only the fields provided by the user
@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book: BookUpdate):
    for existing_book in books:
        if existing_book["id"] == book_id:

            # Extract only the fields explicitly provided in the request
            update_data = book.model_dump(exclude_unset=True)

            if not update_data:
                raise HTTPException(
                    status_code=400,
                    detail="No fields provided for update"
                )

            existing_book.update(update_data)
            return existing_book

    raise HTTPException(status_code=404, detail="Book not found")



# Delete a book by ID and return the deleted book details
@router.delete("/{book_id}", response_model=BookDeleteResponse)
async def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)

            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
# BookStore REST API

A REST API for managing book records, built with **Python**,
**FastAPI**, and **Pydantic**. It supports CRUD operations, filtering
books by title or author, request validation, and automatic API
documentation.

## Features

-   Retrieve all books.
-   Retrieve a single book using its ID.
-   Filter books by title and/or author.
-   Add a new book with Pydantic validation.
-   Update an existing book.
-   Delete a book.
-   Return appropriate HTTP status codes and error messages.
-   Explore and test endpoints through Swagger UI.

## Technology Stack

-   Python 3.10+
-   FastAPI
-   Pydantic
-   Uvicorn

## Project Structure

``` text
BookStore_REST_API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       └── books.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Open the project directory

Open a terminal in the `BookStore_REST_API` root directory.

### 2. Create a virtual environment

**Windows PowerShell**

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Start the development server

Run this command from the project root:

``` bash
uvicorn app.main:app --reload
```

The API runs at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI generates interactive documentation automatically:

-   **Swagger UI:** `http://127.0.0.1:8000/docs`
-   **ReDoc:** `http://127.0.0.1:8000/redoc`
-   **OpenAPI JSON:** `http://127.0.0.1:8000/openapi.json`

Use Swagger UI to send requests and inspect responses.

## API Endpoints

  --------------------------------------------------------------------------
  HTTP Method       Endpoint             Description       Success Status
  ----------------- -------------------- ----------------- -----------------
  GET               `/books/`            Get all books;    200 OK
                                         supports optional 
                                         title/author      
                                         filters           

  GET               `/books/{book_id}`   Get one book by   200 OK
                                         ID                

  POST              `/books/`            Create a new book 201 Created

  PUT               `/books/{book_id}`   Update a book by  200 OK
                                         ID                

  DELETE            `/books/{book_id}`   Delete a book by  200 OK
                                         ID                
  --------------------------------------------------------------------------

If a requested book ID does not exist, the API returns `404 Not Found`.

## Query Filtering

The `GET /books/` endpoint accepts optional query parameters:

``` text
/books/?title=Python
/books/?author=John
/books/?title=Python&author=John
```

Filtering is case-insensitive and supports partial matches. When both
parameters are provided, both conditions are applied.

## Example: Create a Book

Send a `POST` request to `/books/` with this JSON body:

``` json
{
  "title": "Python Advanced",
  "author": "Roopam",
  "price": 599
}
```

A successful response includes the generated book ID and returns
`201 Created`.

## Pydantic Validation

The `BookCreate` schema validates incoming book data:

-   `title`: string, minimum 2 and maximum 100 characters.
-   `author`: string, minimum 2 and maximum 100 characters.
-   `price`: number greater than 0 and less than or equal to 1000.

The `BookResponse` schema defines the structure returned for book
records. The `BookDeleteResponse` schema defines the delete response.

Invalid request data is rejected by FastAPI/Pydantic, normally with
`422 Unprocessable Entity`.

## Error Responses

  Status Code   Meaning
  ------------- -------------------------------------------------------------
  400           Bad Request --- update request contains no fields to update
  404           Not Found --- requested book ID does not exist
  422           Unprocessable Entity --- request data fails validation

## Data Storage

This project currently uses an in-memory Python list to store books. It
is suitable for demonstrating API and validation concepts, but data is
reset when the server restarts. No database is configured.

## Dependencies

The required packages are listed in `requirements.txt`:

``` text
fastapi
uvicorn[standard]
pydantic
```

## Author

**Roopam Gupta**

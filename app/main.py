from fastapi import FastAPI

# Import the books router from the routes module
from app.routes.books import router as books_router



# Initialize the FastAPI application
app = FastAPI(
    title="BookStore API",
    description="A REST API for managing books",
    version="1.0.0"
)

# Register the books router with the main application
app.include_router(books_router)
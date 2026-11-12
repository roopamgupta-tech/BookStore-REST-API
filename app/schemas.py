from pydantic import BaseModel, Field, model_validator


# Schema for validating data when creating a new book
class BookCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    author: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0, le=1000)


# Schema for updating existing book details
class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=100)
    author: str | None = Field(default=None, min_length=2, max_length=100)
    price: float | None = Field(default=None, gt=0, le=1000)

    # Reject explicitly provided null values during updates
    @model_validator(mode="after")
    def reject_null_values(self):
        for field in self.model_fields_set:
            if getattr(self, field) is None:
                raise ValueError(f"{field} cannot be null")
        return self


# Schema for formatting book data in API responses
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float


# Schema for formatting the response after deleting a book
class BookDeleteResponse(BaseModel):
    message: str
    book: BookResponse
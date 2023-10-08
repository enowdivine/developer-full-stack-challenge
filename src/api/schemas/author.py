from pydantic import BaseModel


class AuthorSchema(BaseModel):
    author_name: str
    number_of_books: int

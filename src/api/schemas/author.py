from pydantic import BaseModel


class AuthorSchema(BaseModel):
    user_id: int
    author_name: str
    number_of_books: int

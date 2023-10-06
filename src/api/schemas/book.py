from pydantic import BaseModel


class BookSchema(BaseModel):
    user_id: int
    book_name: str
    author_name: str
    number_of_pages: int

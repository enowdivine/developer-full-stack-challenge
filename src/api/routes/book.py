from fastapi import APIRouter
from config.db import connection
from models.book import booksTable
from schemas.book import BookSchema

book_router = APIRouter()


@book_router.get("/books")
def fetch_book():
    return connection.execute(booksTable.select()).fetchall()


@book_router.post("/add-book")
def add_book(book: BookSchema):
    connection.execute(
        booksTable.insert().values(
            user_id=book.user_id,
            book_name=book.book_name,
            author_name=book.author_name,
            number_of_pages=book.number_of_pages,
        )
    )
    return connection.execute(booksTable.select()).fetchall()


@book_router.put("/update-book/{bookId}")
def update_book(book: BookSchema, bookId: int):
    connection.execute(
        booksTable.update()
        .values(
            book_name=book.book_name,
            author_name=book.author_name,
            number_of_pages=book.number_of_pages,
        )
        .where(booksTable.c.id == bookId)
    )
    return connection.execute(
        booksTable.select().where(
            booksTable.c.id == bookId,
        )
    )


@book_router.delete("/delete-book/{bookId}")
def delete_book(booksTable: BookSchema, bookId: int):
    connection.execute(book.delete().where(booksTable.c.id == bookId))
    return connection.execute(
        booksTable.select().where(
            booksTable.c.id == bookId,
        )
    )

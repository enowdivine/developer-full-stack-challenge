from fastapi import APIRouter, Body
from typing import Any
from config.db import connection
from schemas.user import UserSchema
from schemas.book import BookSchema
from auth.auth import get_current_active_user
from fastapi import Depends
from . import utils

book_router = APIRouter()


# Get all books from database
@book_router.get("/books")
def fetch_books(user: UserSchema = Depends(get_current_active_user)):
    cursor = connection.cursor()
    result = cursor.execute(
        """
    SELECT * FROM booksTable
    """
    ).fetchall()
    data = utils.format_result(cursor=cursor, result=result)
    return data


# Add book to database
@book_router.post("/add-book", response_model=BookSchema)
def add_book(payload: BookSchema, user: UserSchema = Depends(get_current_active_user)):
    print(payload)
    cursor = connection.cursor()
    cursor.execute(
        f"""
    INSERT INTO booksTable (author_id, book_name, author_name, number_of_pages)
    VALUES (?, ?, ?, ?);
    """,
        (
            payload.author_id,
            payload.book_name,
            payload.author_name,
            payload.number_of_pages,
        ),
    )
    connection.commit()
    return {
        "book_name": payload.book_name,
        "author_id": payload.author_id,
        "author_name": payload.author_name,
        "number_of_pages": payload.number_of_pages,
    }


# Update single book from database
@book_router.put("/update-book")
def update_book(
    payload: Any = Body(None), user: UserSchema = Depends(get_current_active_user)
):
    book_id = payload["id"]
    author_id = payload["author_id"]
    book_name = payload["book_name"]
    author_name = payload["author_name"]
    number_of_pages = payload["number_of_pages"]

    cursor = connection.cursor()
    cursor.execute(
        f"""
    UPDATE booksTable
    SET book_name = '{book_name}', author_id = {author_id}, author_name = '{author_name}', number_of_pages = '{number_of_pages}' 
    WHERE id = {book_id}
    """
    )
    connection.commit()
    return {
        "book_name": book_name,
        "author_name": author_name,
        "number_of_pages": number_of_pages,
    }


# Delete book from database
@book_router.delete("/delete-book")
def delete_book(
    payload: Any = Body(None), user: UserSchema = Depends(get_current_active_user)
):
    book_id = payload["id"]
    cursor = connection.cursor()
    cursor.execute(
        f"""
    DELETE FROM booksTable WHERE id={book_id}
    """
    )
    connection.commit()
    return True

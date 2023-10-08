from fastapi import APIRouter, Body
from typing import Any
from config.db import connection
from schemas.author import AuthorSchema
from schemas.user import UserSchema
from auth.auth import get_current_active_user
from fastapi import Depends
from . import utils

author_router = APIRouter()


@author_router.get("/authors")
def fetch_author(user: UserSchema = Depends(get_current_active_user)):
    cursor = connection.cursor()
    result = cursor.execute(
        """
    SELECT * FROM authorsTable
    """
    ).fetchall()
    data = utils.format_result(cursor=cursor, result=result)
    return data


@author_router.get("/author-books/{author_id}")
def number_of_books_per_author(
    author_id, user: UserSchema = Depends(get_current_active_user)
):
    # author_id = payload["id"]
    cursor = connection.cursor()
    result = cursor.execute(
        f"""
    SELECT * FROM booksTable WHERE author_id={author_id}
    """
    ).fetchall()
    data = utils.format_result(cursor=cursor, result=result)
    return data


@author_router.post("/add-author", response_model=AuthorSchema)
def add_author(
    payload: AuthorSchema, user: UserSchema = Depends(get_current_active_user)
):
    print(payload)
    cursor = connection.cursor()
    cursor.execute(
        """
    INSERT INTO authorsTable (author_name, number_of_books)
    VALUES (?, ?)
    """,
        (payload.author_name, payload.number_of_books),
    )
    connection.commit()
    return {
        "author_name": payload.author_name,
        "number_of_books": payload.number_of_books,
    }


@author_router.put("/update-author")
def update_author(
    payload: Any = Body(None), user: UserSchema = Depends(get_current_active_user)
):
    author_id = payload["id"]
    author_name = payload["author_name"]
    cursor = connection.cursor()
    cursor.execute(
        f"""
    UPDATE authorsTable
    SET author_name = '{author_name}'
    WHERE id = {author_id}
    """
    )
    cursor.execute(
        f"""
    UPDATE booksTable
    SET author_name = '{author_name}'
    WHERE author_id = {author_id}
    """
    )
    connection.commit()
    return {"author_name": author_name}


@author_router.delete("/delete-author")
def delete_author(
    payload: Any = Body(None), user: UserSchema = Depends(get_current_active_user)
):
    author_id = payload["id"]
    cursor = connection.cursor()
    cursor.execute(
        f"""
    DELETE FROM authorsTable WHERE id={author_id}
    """
    )
    connection.commit()
    return True

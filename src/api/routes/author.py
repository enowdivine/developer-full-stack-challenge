from fastapi import APIRouter
from config.db import connection
from models.author import authorsTable
from schemas.author import AuthorSchema

author_router = APIRouter()


@author_router.get("/authors")
def fetch_author():
    return connection.execute(authorsTable.select()).fetchall()


@author_router.post("/add-author")
def add_author(author: AuthorSchema):
    connection.execute(
        authorsTable.insert().values(
            user_id=author.user_id, author_name=author.author_name
        )
    )
    return connection.execute(authorsTable.select()).fetchall()


@author_router.put("/update-author/{authorId}")
def update_author(author: AuthorSchema, authorId: int):
    connection.execute(
        authorsTable.update()
        .values(author_name=author.author_name)
        .where(authorsTable.c.id == authorId)
    )
    return connection.execute(
        authorsTable.select().where(
            authorsTable.c.id == authorId,
        )
    )


@author_router.delete("/delete-author/{authorId}")
def delete_author(author: AuthorSchema, authorId: int):
    connection.execute(authorsTable.delete().where(authorsTable.c.id == authorId))
    return connection.execute(
        authorsTable.select().where(
            authorsTable.c.id == authorId,
        )
    )

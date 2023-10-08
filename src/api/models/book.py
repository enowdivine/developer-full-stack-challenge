from sqlalchemy import INTEGER, Column, String, Table
from config.db import meta, engine


booksTable = Table(
    "booksTable",
    meta,
    Column("id", INTEGER, primary_key=True),
    Column("author_id", INTEGER, nullable=False),
    Column("book_name", String(16), nullable=False),
    Column("author_name", String(16), nullable=False),
    Column("number_of_pages", INTEGER, nullable=False),
)

meta.create_all(engine)

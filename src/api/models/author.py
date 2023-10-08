from sqlalchemy import INTEGER, Column, String, Table
from config.db import meta, engine

authorsTable = Table(
    "authorsTable",
    meta,
    Column("id", INTEGER, primary_key=True),
    Column("author_name", String(16), nullable=False),
    Column("number_of_books", INTEGER, nullable=False),
)

meta.create_all(engine)

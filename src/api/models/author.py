from sqlalchemy import INTEGER, Column, String, Table
from config.db import meta, engine


def mydefault(context):
    return context.get_current_parameters()[0]


authorsTable = Table(
    "authorsTable",
    meta,
    Column("id", INTEGER, primary_key=True),
    Column("user_id", INTEGER, nullable=False),
    Column("author_name", String(16), nullable=False),
    Column("number_of_books", INTEGER, default=mydefault),
)

meta.create_all(engine)

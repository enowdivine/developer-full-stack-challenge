from sqlalchemy import INTEGER, Boolean, Column, String, Table
from config.db import meta, engine

usersTable = Table(
    "usersTable",
    meta,
    Column("id", INTEGER, primary_key=True),
    Column("username", String(255), nullable=False),
    Column("password", String(255), nullable=False),
)

meta.create_all(engine)

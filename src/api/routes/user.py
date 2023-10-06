from fastapi import APIRouter
from config.db import connection
from models.user import usersTable
from schemas.user import UserSchema

user_router = APIRouter()


@user_router.get("/user")
def fetch_user():
    return connection.execute(usersTable.select()).fetchall()


@user_router.post("/user-login")
def login_user(user: UserSchema):
    # print(user)
    connection.execute(
        usersTable.insert().values(username=user.username, password=user.password)
    )
    return connection.execute(usersTable.select()).fetchall()

from fastapi import APIRouter
from config.db import connection
from auth.auth import (
    Token,
    authenticate_user,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from . import utils
from schemas.user import UserSchema


# authentication imports
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from datetime import timedelta

user_router = APIRouter()


# Login endpoint to get authenticated
@user_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print(type(form_data))
    allusers = utils.get_all_users()
    dbusers = {item["username"]: item for item in allusers}
    user = authenticate_user(dbusers, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Add new user with hashed password to database
@user_router.post("/add-user", response_model=UserSchema)
def add_user(payload: UserSchema):
    cursor = connection.cursor()
    cursor.execute(
        """
    INSERT INTO usersTable (username, password)
    VALUES (?, ?)
    """,
        (payload.username, payload.password),
    )
    connection.commit()
    return {"username": payload.username, "password": payload.password}


# Get all users from database
@user_router.get("/users")
def fetch_user():
    cursor = connection.cursor()
    result = cursor.execute(
        """
    SELECT * FROM usersTable
    """
    ).fetchall()
    print("success")
    data = utils.format_result(cursor=cursor, result=result)
    return data

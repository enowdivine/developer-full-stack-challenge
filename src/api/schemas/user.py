from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class UserSchema(BaseModel):
    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password

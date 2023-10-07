from pydantic import BaseModel, ValidationError
from pydantic.dataclasses import dataclass


@dataclass
class UserSchema(BaseModel):
    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password


# m = UserSchema.model_validate({"username": "mike", "password": "tester"})
# print(m)

try:
    UserSchema.model_validate("not an object")
except ValidationError as exc:
    print(repr(exc.errors()[0]["type"]))

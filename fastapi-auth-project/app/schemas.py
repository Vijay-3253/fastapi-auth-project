from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("password")
    def password_max_bytes(cls, value: str):
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must be 72 bytes or fewer for bcrypt hashing")
        return value

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
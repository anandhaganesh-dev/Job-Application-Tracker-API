from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=64)


class UserResponse(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str

    class ConfigDict:
        from_attributes = True

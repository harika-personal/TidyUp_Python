from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class BaseAuthResponse(BaseModel):
    message: str
    token: str
    user: UserResponse

class UserSignupResponse(BaseAuthResponse):
    pass

class UserLoginResponse(BaseAuthResponse):
    pass
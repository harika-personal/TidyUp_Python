from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserSignupResponse, UserLoginResponse, UserLogin
from app.models import User
from sqlalchemy import select
from passlib.context import CryptContext
from app.utils.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/test")
def test_endpoint():
    return{"message" : "Auth router is working"}

@router.post("/signup", response_model=UserSignupResponse, status_code=status.HTTP_201_CREATED)
def signup(user_data:UserCreate, db: Session = Depends(get_db)):
    existing_user = db.execute(select(User).where(User.email == user_data.email)).scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered"
        )
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(
        name = user_data.name,
        email =user_data.email,
        password = hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(data={"sub": str(new_user.id), "email": new_user.email})

    return {
        "message": "User created successfully",
        "token": token,
        "user": new_user

    }

@router.post("/login", response_model=UserLoginResponse, status_code=status.HTTP_200_OK)
def login(user_data:UserLogin, db: Session = Depends(get_db)):
    existing_user = db.execute(select(User).where(User.email == user_data.email)).scalar_one_or_none()

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )

    valid_password = pwd_context.verify(user_data.password, existing_user.password)

    if not valid_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )

    token = create_access_token(data={"sub": str(existing_user.id), "email": existing_user.email})

    return {
        "message": "Login Successful!",
        "token": token,
        "user": existing_user
    }

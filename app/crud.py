from sqlalchemy.orm import Session
from app import models
from app.auth import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, email: str, password: str):
    hashed = hash_password(password)
    user = models.User(username=username, email=email, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
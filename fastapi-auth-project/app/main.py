from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router)
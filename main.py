from fastapi import FastAPI, HTTPException
from app.routes.issues import router as issues_router

app = FastAPI()

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

app.include_router(issues_router)
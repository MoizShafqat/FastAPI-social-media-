from operator import index
from fastapi import Body, Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas, util
from .database import SessionLocal, engine
from .routers import post, user, auth, vote
import time



models.Base.metadata.create_all(engine)

app = FastAPI()

try:
    conn = psycopg2.connect(host='localhost' , database='fastapi', user='postgres', password='allah@123', cursor_factory=RealDictCursor)
    cur = conn.cursor()
except Exception as error:
    print("Error connecting to PostgreSQL:")
    print("Error;", error)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router) 


@app.get("/")
def read_root():
    return {"Hello": "welcome to FastAPI!!!!"}

# @app.get("/sqlalchemy")
# def test_post( db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}


#Retrieve all posts from database

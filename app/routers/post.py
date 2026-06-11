from ..import models, schemas 
from fastapi import APIRouter, Depends, HTTPException, status , Response , FastAPI
from sqlalchemy.orm import Session
from ..database import get_db
from app import oauth2
router = APIRouter(tags=["Posts"])

@router.get("/post", response_model=list[schemas.Post])
def get_post(db: Session = Depends(get_db)):
    # cur.execute("""SELECT * From posts""")
    # post = cur.fetchall()
    posts = db.query(models.Post).all()
    return  posts




#create a post in the memory
@router.post("/createposts", response_model=schemas.Post)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user)  
):
    
    print(user_id)

    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/post/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user)):
 print(user_id)
    # cur.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    # posttest = cur.fetchone()
 post = db.query(models.Post).filter(models.Post.id == id).first()

 if not post:
       raise HTTPException(status_code=404, detail="Post not found")

 return post
    # return {"data": posttest}

@router.delete("/post/{id}")
def deletepost(id: int, db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user)):
    print(user_id)
    # cur.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
    # deleted_post = cur.fetchone()
    # conn.commit()

    deleted_post = db.query(models.Post).filter(models.Post.id == id).first()

    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(deleted_post)
    db.commit()

    return {"message": "Deleted successfully"}
    return {"error": "Post not found"}

    return {"message": "Deleted successfully"}


@router.put("/post/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user)):
    print(user_id)
    existing_post = db.query(models.Post).filter(models.Post.id == id).first()

    if not existing_post:
        raise HTTPException(status_code=404, detail="Post not found")

    existing_post.title = post.title
    existing_post.content = post.content
    existing_post.published = post.published
    db.commit()
    db.refresh(existing_post)

    return existing_post 
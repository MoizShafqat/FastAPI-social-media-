# FastAPI Social Media API

A RESTful API built with FastAPI, PostgreSQL, and JWT authentication.

## Features
- User registration and login with JWT
- Create, read, update, delete posts
- Like/unlike posts (vote system)
- Protected routes
- Password hashing with bcrypt

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- bcrypt
- Pydantic

## Installation

1. Clone the repository
git clone https://github.com/YOURUSERNAME/fastapi-social-media.git

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
DATABASE_URL=postgresql://username:password@localhost/fastapi_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Run the application
uvicorn app.main:app --reload

6. Open API docs
http://127.0.0.1:8000/docs
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import random
import string
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Isha@1608@localhost:5432/urlshortener")

import urllib.parse
result = urllib.parse.urlparse(DATABASE_URL)

conn = psycopg2.connect(
    host=result.hostname,
    database=result.path[1:],
    user=result.username,
    password=result.password,
    port=result.port
)


cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id SERIAL PRIMARY KEY,
        short_code VARCHAR(10) UNIQUE NOT NULL,
        original_url TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        click_count INTEGER DEFAULT 0
    )
""")
conn.commit()

# Model
class URLRequest(BaseModel):
    url: str

# Generate random short code
def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.get("/")
def read_root():
    return {"message": "URL Shortener API is running"}

@app.post("/shorten")
def shorten_url(request: URLRequest):
    code = generate_code()
    cursor.execute(
        "INSERT INTO urls (short_code, original_url) VALUES (%s, %s)",
        (code, request.url)
    )
    conn.commit()
    return {"short_code": code, "short_url": f"http://localhost:8000/{code}"}

@app.get("/{short_code}")
def redirect_url(short_code: str):
    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code = %s", (short_code,)
    )
    result = cursor.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")
    cursor.execute(
        "UPDATE urls SET click_count = click_count + 1 WHERE short_code = %s", (short_code,)
    )
    conn.commit()
    return {"original_url": result[0]}

@app.get("/analytics/{short_code}")
def get_analytics(short_code: str):
    cursor.execute(
        "SELECT original_url, click_count, created_at FROM urls WHERE short_code = %s",
        (short_code,)
    )
    result = cursor.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")
    return {
        "original_url": result[0],
        "click_count": result[1],
        "created_at": result[2]
    }
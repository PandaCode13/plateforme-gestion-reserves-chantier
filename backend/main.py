import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title="Backend")

frontend_origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:3000")

@app.get("/health-check")
def health_check():
    return {"status": "healthy"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in frontend_origins.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    # Example data to return
    data = {
        "message": "Hello from the backend!",
        "items": [1, 2, 3, 4, 5]
    }
    return data

from fastapi import FastAPI

from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import exercises, workouts, accounts

app = FastAPI()
app.include_router(authenticator.router, prefix="/api/auth")
app.include_router(exercises.router, prefix="/api/exercises")
app.include_router(workouts.router, prefix="/api/workouts")
app.include_router(accounts.router, prefix="/api/accounts")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("http://localhost:3000", "http://localhost:8000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }

from fastapi import FastAPI

from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import exercises, workouts, accounts, auth

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    os.environ.get("CORS_HOST"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    exercises.router, prefix="/api/exercises", tags=["exercises"]
)
app.include_router(workouts.router, prefix="/api/workouts", tags=["workouts"])
app.include_router(accounts.router, prefix="/api/accounts", tags=["Accounts"])
app.include_router(auth.router, tags=["Auth"])

app.include_router(authenticator.router, tags=["Login/Logout"])

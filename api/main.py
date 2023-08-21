from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from authenticator import authenticator
from routers import accounts


app = FastAPI()
app.include_router(authenticator.router)
app.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
#^ allows a label addition to the fastapi browser

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

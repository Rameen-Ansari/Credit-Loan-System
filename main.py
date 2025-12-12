from fastapi import FastAPI
from App.DB.session import engine
from App.DB.base import base
from App.Models import user

app=FastAPI(title="Credit & Loan Backend",version="1.0")

@app.on_event("startup")
def on_startup():
    base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status":"ok","message":"service running"}


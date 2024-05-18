from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user
from app.db import startup_db_client, shutdown_db_client

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# user 라우터를 포함시키고, 모든 경로 앞에 "/users" 접두사를 추가
app.include_router(user.router, prefix="/users")

@app.on_event("startup")
async def on_startup():
    await startup_db_client()

@app.on_event("shutdown")
async def on_shutdown():
    await shutdown_db_client()
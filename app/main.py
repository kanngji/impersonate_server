from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user
from app.db import startup_db_client, shutdown_db_client
from contextlib import asynccontextmanager

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("FastAPI 애플리케이션 시작",flush=True)
    await startup_db_client()
    print("DB 클라이언트 초기화 완료",flush=True)
    yield
    print("FastAPI 애플리케이션 종료",flush=True)
    await shutdown_db_client()
    print("DB 클라이언트 종료 완료",flush=True)

app = FastAPI(lifespan=lifespan)

from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 origin 허용, 필요에 따라 수정 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

uri = os.getenv("DB_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# FastAPI 앱 시작 시 MongoDB 연결
@app.on_event("startup")
async def startup_db_client():
    try:
        # MongoDB에 ping을 보내서 연결을 확인
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("error")

# FastAPI 앱 종료 시 MongoDB 연결 닫기
@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()



@app.get("/hello")
async def hello():
    return {"message":"안녕하세요"}
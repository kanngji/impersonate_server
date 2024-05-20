from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("DB_URI")
if uri is None:
    print("환경변수 x", flush=True)
print(f"Connecting to MongoDB at",flush=True)  # 추가된 로그
client = MongoClient(uri, server_api=ServerApi('1'))

async def startup_db_client():
    print("데이터베이스 초기화 시작",flush=True)  # 추가된 로그
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!",flush=True)
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}",flush=True)

async def shutdown_db_client():
    print("데이터베이스 클라이언트 종료",flush=True)  # 추가된 로그
    client.close()
    print("데이터베이스 클라이언트 종료 완료",flush=True)  # 추가된 로그
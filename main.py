# utils
import requests
from datetime import datetime
import uvicorn
from typing import Union, Dict, List
import random
import shutil

# FastAPI
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware

# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()
import os

UPLOAD_DIR = "./files"

# request
class GachaSpinRequest(BaseModel):
    user_id: int
    gacha_id: int

class UserBalanceRequest(BaseModel):
    user_id: int

class GachaDetailRequest(BaseModel):
    gacha_id: int

class RegisterNFTRequest(BaseModel):
    nft_name: str

# response
class GachaSpinResponse(BaseModel):
    gacha_id: int
    contents: list [ int ]

class GachaBalanceResponse(BaseModel):
    user_id: int
    balance_yen: int

# FastAPIサーバー部分
app = FastAPI()

# avoid CORS
# https://qiita.com/satto_sann/items/0e1f5dbbe62efc612a78
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

# for testing
@app.get("/api/test")
def api_test():
    a = "a"
    b = "b" + a
    return {"hello world": b}

# login
@app.post("/api/login")
async def password_login():
    pass

# list owned
@app.post("/api/user/balance", response_model=UserBalanceRequest)
async def user_balance(request: UserBalanceRequest):
    pass


# spin
@app.post("/api/gacha/spin", response_model=GachaSpinRequest)
async def gacha_spin(request: GachaSpinRequest):
    
    return

# admin
@app.post("/api/gacha/register")
async def gacha_register(file: UploadFile = File(...)):
    if file:
        filename = file.filename
        fileobj = file.file
        upload_dir = open(os.path.join(UPLOAD_DIR, filename),'wb+')
        shutil.copyfileobj(fileobj, upload_dir)
        upload_dir.close()
        return {"アップロードファイル名": filename}
    return {"Error": "アップロードファイルが見つかりません。"}

@app.post("/api/nft/register")
async def nft_register():
    pass


# launch
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# utils
import requests
from datetime import datetime
import uvicorn
from typing import Union, Dict, List
import random

# FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware

# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()
import os


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


# launch
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# publicRoom.jsonを読み込む関数
def load_publicRooms():
    publicRoom_file = Path("data/publicRoom.json")  # publicRoom.jsonのパス
    if publicRoom_file.exists():
        with publicRoom_file.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []  # ファイルがない場合は空のリストを返す

# privateRoom.jsonを読み込む関数
def load_privateRooms():
    privateRoom_file = Path("data/privateRoom.json")  # privateRoom.jsonのパス
    if privateRoom_file.exists():
        with privateRoom_file.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []  # ファイルがない場合は空のリストを返す

@app.get("/")
def Hello():
    return {"Hello":"World!"}

# RoomのJSONデータを返すエンドポイント
@app.get("/publicRooms")
def get_publicRooms():
    return load_publicRooms()

# RoomのJSONデータを返すエンドポイント
@app.get("/publicRooms/{room_id}")
def get_publicRoom(room_id: int):
    publicRooms = load_publicRooms()
    for room in publicRooms:
        if room["id"] == room_id:
            return room
    return {"error": "Room not found"}

# privateRoomのJSONデータを返すエンドポイント
@app.get("/privateRooms")
def get_privateRooms():
    return load_privateRooms()

@app.get("/privateRooms/{room_id}")
def get_privateRoom(room_id: int):
    privateRooms = load_privateRooms()
    for room in privateRooms:
        if room["id"] == room_id:
            return room
    return {"error": "Room not found"}
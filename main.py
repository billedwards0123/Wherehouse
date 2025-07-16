from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parent
INVENTORY_FILE = DATA_DIR / "inventory.json"
TASKS_FILE = DATA_DIR / "tasks.json"
CHAT_FILE = DATA_DIR / "chat.json"

app = FastAPI(title="P.A.M. Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility functions ----------------------------------------------------------

def load_json(path: Path, default):
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def log_update(entry: dict):
    entry["timestamp"] = datetime.utcnow().isoformat()

# Data models ---------------------------------------------------------------

class InventoryItem(BaseModel):
    name: str
    location: str
    quantity: int
    par_level: int

class Task(BaseModel):
    id: int
    description: str
    assigned_to: str
    status: str = "open"
    notes: str = ""

class ChatMessage(BaseModel):
    sender: str
    message: str

# Routes --------------------------------------------------------------------

@app.get("/inventory", response_model=List[InventoryItem])
def get_inventory():
    return load_json(INVENTORY_FILE, [])

@app.post("/inventory", response_model=InventoryItem)
def update_inventory(item: InventoryItem):
    items = load_json(INVENTORY_FILE, [])
    for idx, existing in enumerate(items):
        if existing["name"] == item.name and existing["location"] == item.location:
            items[idx] = item.dict()
            log_update(items[idx])
            save_json(INVENTORY_FILE, items)
            return item
    items.append(item.dict())
    log_update(items[-1])
    save_json(INVENTORY_FILE, items)
    return item

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return load_json(TASKS_FILE, [])

@app.post("/tasks", response_model=Task)
def add_or_update_task(task: Task):
    tasks = load_json(TASKS_FILE, [])
    for idx, existing in enumerate(tasks):
        if existing["id"] == task.id:
            tasks[idx] = task.dict()
            log_update(tasks[idx])
            save_json(TASKS_FILE, tasks)
            return task
    tasks.append(task.dict())
    log_update(tasks[-1])
    save_json(TASKS_FILE, tasks)
    return task

@app.get("/chat", response_model=List[ChatMessage])
def get_chat():
    return load_json(CHAT_FILE, [])

@app.post("/chat", response_model=ChatMessage)
def post_chat(msg: ChatMessage):
    history = load_json(CHAT_FILE, [])
    entry = msg.dict()
    log_update(entry)
    history.append(entry)
    save_json(CHAT_FILE, history)
    return msg


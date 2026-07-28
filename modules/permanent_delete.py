import os
import json
from datetime import datetime

TOKEN_FILE="data/delete_tokens.json"
HISTORY_FILE="data/delete_history.json"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path,"r") as f:
        return json.load(f)

def save_json(path,data):
    os.makedirs("data",exist_ok=True)
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

def permanent_delete(token):
    tokens=load_json(TOKEN_FILE)
    if token not in tokens:
        return {"success":False,"error":"Invalid token"}
    path=tokens[token]["path"]
    if not os.path.exists(path):
        return {"success":False,"error":"File not found"}
    history=load_json(HISTORY_FILE)
    history[str(len(history)+1)]={
        "path":path,
        "deleted_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    os.remove(path)
    del tokens[token]
    save_json(TOKEN_FILE,tokens)
    save_json(HISTORY_FILE,history)
    return {"success":True}
